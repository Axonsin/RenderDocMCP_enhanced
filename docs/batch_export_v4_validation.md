# 4.0 批量导出验证（2026-11-04）

## 自动化检查

- `python -m pytest tests -q`：317 passed，98 subtests passed。
- `python scripts/check_contracts.py`：46 个工具，schema 与文档同步；
  35 个扩展 Python 文件通过 Python 3.6 语法检查。
- `git diff --check`：通过。
- 全局安装的 MCP server 的 6 个 Python 文件与仓库源码逐一比对一致。

测试覆盖完整清单、多阶段网格、跨事件纹理、mip/layer 选择、EXR 预览、Shader
共享与管线特化区分、取消/额度暂停、重新创建 JobService 后恢复、捕获/构建/选项
不匹配拒绝、损坏文件补导、常量失败后继续导出其他资产、回放失联立即停止、
Windows 参数转义、原子快照共享冲突、有界状态等待和扩展重载依赖。

## Android Vulkan 实测

环境：RenderDoc 1.46，LENOVO TB322FC，`adb://HA29QMVJ`。
捕获：GFL2 frame21389；SHA256：
`aaf18a8d9505e2f5be1f7184d89570c9bb7f457d2b7b2909f7eb1e73dad7eab2`。
事件：681、739。测试通过正式 MCP stdio 工具执行，未使用扩展内 run_script，
未应用 Shader replacement，未注入设备故障。

流程：提交批次（纹理额度 2）→ 暂停 → 取消 → RenderDoc 重载扩展 →
重开捕获 → resume_job → 完成 → 校验 checkpoint 中每份文件的 SHA256 →
检查连接健康、当前事件和构建身份。

| 案例 | 完成的产物任务 | 复用任务 | 失败任务 | 核对的文件记录 |
| --- | ---: | ---: | ---: | ---: |
| 完整 bound mip/layer，构建 `2de25f0e…` | 326 | 14 | 0 | 502 |
| 最终发布构建 `9eeae30f…`，mip 0、全部 bound layer | 72 | 14 | 0 | 121 |

“任务”包含绑定、常量、网格、Shader、HLSL 和纹理产物；文件记录可能引用共享的
常量 blob，不等于独立文件数。两个案例都导出 4 份网格（两种阶段 × 两个 draw）、
4 组 Shader 及其 HLSL、12 组常量。完整 bound 案例包含 300 份纹理产物。
两个案例最终均为 completed，回放健康，事件恢复为 951，回放修订为 0。

最终发布构建全指纹：
`9eeae30f5944f1bbf974c50cf25cfa7a759a0b9c756f2457055f514ce847e76c`。
完整 bound 案例之后补充了常量 blob 修复和错误明细保留；最终构建另行完成了
相同取消/重载/重开/恢复流程，明确限制到 mip 0。多 mip 行为由完整案例和单元测试覆盖。

## 实测发现并修复的问题

- Windows 快照读取与原子替换偶发共享冲突：读写两端只重试同一文件操作，
  最多 7 次，等待总量不超过约 0.315 秒；不重提原生导出。
- 新模块未加入重载依赖时会保留旧 PauseJob 类：补全按依赖排序的模块重载列表，
  并加入回归检查。实际跨重载暂停/恢复已验证。
- os.spawnv 在 Windows 不自动转义空格：为独立参数实现 CRT 转义，并通过真实
  子进程验证空格、引号、反斜杠和 Unicode。HLSL 使用临时输出再原子替换。
- 损坏的内容寻址常量 blob：只有在批次身份验证后，才允许使用重新读取的捕获字节
  修复；其他调用保留默认的哈希不匹配拒绝行为。

## 证据与复现

外部证据目录：

- `D:/Unity_Projects/GamesRenderReplica_evidence/diagnostics/durable_batch_v4_verified/`
- `D:/Unity_Projects/GamesRenderReplica_evidence/diagnostics/durable_batch_v4_release/`

每个目录的 live_validation.json 保存作业状态、健康状态、构建身份和核对计数；
export/<job_id>/ 保存计划、checkpoint、统一清单、阶段计时及全部产物。

复现使用 `scripts/validate_batch_live.py --phase prepare`，在 UI 重载扩展，
然后使用同一输出目录运行 `--phase resume`。观察既有任务可用 `--phase observe`，
不会重提导出。`--mip-zero` 只缩小实测范围，不改变产品默认配置。

本机 RTX 4070 SUPER 不支持该捕获要求的 VK_EXT_astc_decode_mode，因此该捕获的
本机回放没有作为通过依据；用户接回 Android 设备后完成了上述远程验证。
其他 GPU/API、volume preview，以及单次原生调用本身挂起不在本次实测通过范围内。
卷纹理可保留 raw；原生调用不能强制中断。升级方式与功能限制见 migration_v4.md。
