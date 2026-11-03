# 4.0 完整批量导出与迁移

服务器和 RenderDoc 扩展必须成套升级到 **4.0.0 / API contract 4**。
文件 IPC 仍为 2。旧客户端会被明确拒绝；重连 MCP 客户端以刷新工具参数。
旧版作业不能迁移为持久化任务，需要重新提交一次导出。

## 唯一导出路径

`dump_draws` 移除了单值 `mesh_stage`、`export_meshes`、`export_textures`。
使用 `export_options.mesh_stages` 和 `texture_modes`，空列表关闭对应组件。
不再维护旧版导出引擎。

```python
job = dump_draws(
    output_dir="D:/exports/frame21389",
    action_event_ids=[681, 739],
    instances=[0], view_index=0,
    export_constants=True, max_textures=48,
    export_options={
        "mesh_stages": ["VSIn", "VSOut"],
        "shader_stages": ["vertex", "fragment"],
        "disassembly_targets": ["default"],
        "texture_modes": ["preview", "raw"],
        "preview_format": "PNG",
        "mips": "bound", "slices": "bound", "samples": [0],
        "aspects": ["all"],
        "hlsl_converter": "C:/Program Files/RenderDoc/plugins/spirv/spirv-cross.exe"
    })
```

上面展示默认配置，唯独 HLSL 转换默认关闭。`hlsl_converter` 必须为已经安装的
SPIRV-Cross 的绝对路径。转换在 CPU worker 中以原始 SPIR-V 为输入执行，保存
转换器哈希与参数；不修改原始证据，也不会自动创建 Unity 材质。
HLSL 转换与其他 CPU 任务不占用回放线程。

- `mesh_stages`：VSIn / VSOut / GSOut。VSIn 的 view 固定为 0，其他阶段用 view_index。
- `shader_stages`：规范阶段名或别名；未绑定的阶段不导出。
- `disassembly_targets`：`["default"]` 选择第一个可用通用目标；`[]` 关闭；
  `null` 导出所有目标；也可填写准确目标名称。单独的 `export_shader_bundle` 同样支持。
- `texture_modes`：preview / raw；预览格式 PNG / EXR / DDS。预览是可视转换。
  raw 是数值数据，保存来源格式、颜色空间、端序及可用的布局信息。
- `mips` / `slices` / `samples`：`"all"`、`"bound"` 或非负索引列表。
  bound 的 mip、slice 覆盖 descriptor 范围；sample 的 bound 为 0。
  立方体面作为 slice 导出，卷纹理的 raw 保留完整 mip 深度；卷预览明确报不支持。
- `aspects`：all / depth / stencil，作用于 raw；深度/模板转换沿用现有已验证格式，
  不支持的转换明确报错。每个原始子资源上限 64 MiB。
- `max_textures`：每次执行的纹理产物额度，preview/raw、mip、层、sample、aspect
  分别计数。耗尽暂停，resume_job 的 texture_budget 提供新额度。

## 清单与恢复

`output_dir/<job_id>/` 包含 plan.json、checkpoint.json、manifest.json、stages.jsonl，
以及网格、Shader 和纹理、逐 draw 的常量文件。完整绑定和状态留在磁盘，工具状态
只返回摘要与路径。plan 固定事件选择和选项；checkpoint 对完成的每个产物记录
路径、SHA256 和字节数。失败任务仍保留已提交的 checkpoint。

先打开同一捕获，再调用：

```python
resume_job(job_id=job["job_id"], texture_budget=96)
```

支持暂停、取消、失败、扩展重载/重启、捕获关闭后重开，以及已完成任务的校验补导。
恢复验证在 worker 中执行，不阻塞 UI 保活。要求本机保留原始 RDC，核对捕获哈希、
API、原始回放、扩展构建、导出选项和转换器哈希；任何不匹配都拒绝复用。
有 Shader replacement 时拒绝提交/恢复，避免把不稳定的替换 ID 当作内容身份。
执行期间捕获会话或回放修订变化仍会中断作业。

恢复不会复用旧会话 binding ID。绑定快照重新获取；文件哈希验证通过才复用。
Shader 按阶段、资源与管线共享；纹理按 EID + 资源 + mip + layer + sample +
导出模式/aspect 分开；常量保留每个 draw 的来源。同一纹理资源在不同事件的内容
不会因为 ResourceId 相同而被跳过。

普通资产失败保留其他成功产物，最终状态为 completed_with_errors；回放失联立即
终止，不会把失败读回标记成功。完成状态只代表证据导出，不代表渲染还原已验收。

## 进度与有界等待

```python
state = get_job_status(job_id=job["job_id"], wait_seconds=10)
state = get_job_status(job_id=job["job_id"], after_revision=state["status_revision"],
                       wait_seconds=10)
```

等待只在 MCP 服务器读取本机原子快照，最长 20 秒，不持有 IPC 调用锁，也不访问
UI 或回放。after_revision 相同且等待超时返回 changed=false、空 items；状态改变或
进入暂停/终态立即返回。设置 wait_for="terminal" 可以忽略中间阶段更新，仅在终态、
暂停或等待期限到达时返回，适合助手等待整个批次，减少工具调用。首次读取不传 after_revision 可以等待下一次状态变化。

状态包含 current_event_id、current_instance、current_resource_id、current_operation、
phase_elapsed_seconds、waiting_for_native、artifact_progress、counts、failures、
pause_reason、cancel_supported/can_request_cancel、status_revision 等字段。
phase_timings 只保留最近 64 个阶段，详细计时见 stages.jsonl。
stalled 只是长时间无进展的观测，不代表原生操作已失败；不会自动重提未知结果的请求。
原生调用不能被强制中断，取消在步骤之间生效。

English summary: this is a breaking release with one durable export engine.
Replace mesh_stage/export_meshes/export_textures with export_options lists.
Durable recovery validates the local capture and each artifact across reloads.
Use bounded, file-only status waits instead of polling replay or arbitrary scripts.
