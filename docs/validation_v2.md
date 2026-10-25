# RenderDoc MCP 2.0 实现与验收记录

日期：2026-10-25。**P0–P2 代码已实现，自动化检查及指定设备的真实 Vulkan 验收通过。post-VS 的索引和完整 xyzw 与 RenderDoc 原生读取一致，按本次验收标准判定通过；恒值现象保留为观察记录。**

## 环境和来源

- 官方依据：RenderDoc v1.46，`e4bd23b671d3d5a747ff5221dbe08a63eb6ca200`，链接见 [迁移说明](migration_v2.md)。
- MCP 包／扩展：2.0.0；API 契约 2；44 个公开 MCP 工具。
- 真实回放：Android `adb://HA29QMVJ`，RenderDoc 1.46，Vulkan。
- 输入：`E:\works\RenderDoc_files\com.studiobside.starMain_2026.10.10_10.07_frame111909.rdc`。
- 捕获 SHA256：`cbe1582ebd0be6c75f4667fcf2ecc53c74468cbd76eca1ed5662f0620868d9a4`。
- 最终源码、部署目录和运行代码指纹一致：`48ad0af9a45ed11dbc65a9420279d87ce41f8a95f90a69774625df29db1adb1a`。
- 较早批次／原生对照指纹另记录在原始请求中；最终补齐了 CaptureContext 上下文同步、
  APK 启动门禁、重复请求计数、非有限值统计以及紧凑状态页／历史详情按需读取，并重跑验收。
- 全局 `renderdoc-mcp` 启动器已修复并升级至 2.0.0，使用锁定依赖离线安装；实际 stdio 连接可发现 44 个工具。

MCP 请求实际经过 FastMCP stdio 客户端、服务器和文件 IPC。独立原生对照明确标为
`independent_native_replay_callback`，在 RenderDoc `BlockInvoke` 回调内读取，没有当作纯 MCP 结果。

## 自动化检查

```powershell
python -m pytest tests -q
.venv\Scripts\python.exe scripts/check_v2_contracts.py
git diff --check
```

- **218 项测试、92 项子测试通过**。包含 D3D 自动化回归，不代表真实 D3D 捕获验收。
- 扩展 29 个 Python 文件通过 Python 3.6 语法检查。
- 版本、最低 RenderDoc 版本、44 个工具 schema、AGENTS／中英文工具名称及共享 skill 引用同步检查通过。
- 差异检查通过。根目录无参数 pytest 曾收集到独立 benchmark 的 NumPy 并发生原生崩溃；
  上述结果明确对应 `tests/`，不将该 benchmark 写成已通过。
- 本地依赖一致性检查通过，失效的旧包元数据移至忽略的证据目录保留，没有删除用户资源。

## 真实设备验收结果

| 检查 | 实测结果 |
|---|---|
| 本地 RDC 上传并远端加载 | 官方上传，回读真实字节并核验 SHA256；实际主机 HA29QMVJ、API Vulkan、健康状态正确 |
| 已装 Android 服务冷启动 | 检查当前用户、原生主 ABI、包数量、versionCode／构建哈希，再走官方启动；启动后重新确认可用，通过 CaptureContext 选择上下文并加载成功；未执行 APK 安装／升级 |
| 已有远端文件加载 | 官方下载预检、`local=False` 加载通过，捕获哈希一致；未创建同名本地占位文件 |
| viewport／scissor／blend | EID 1942 与独立原生字段逐项相同；viewport／scissor 为 2280×1428，blend 为 One／InvSrcAlpha／Add |
| 动态 UBO | EID 169，buffer 5351583，实际 offset 1460992；与原生 GetConstantBlocks 和 64 字节读取一致，未重复叠加 dynamic offset |
| VSIn | EID 949 的有效索引及首个 float32 属性值与独立原生读取一致 |
| post-VS 索引读取 | EID 949 的真实引用为 `[0,3,1,3,0,2]`；MCP 与原生相同，没有错误生成为顺序引用 |
| post-VS 位置读取 | EID 169、633、949、961、1942 的采样索引及完整 position.xyzw 与独立原生读取一致，按原生对照标准通过；恒值观察见下文 |
| 123 draw 长批次 | 作业 `7270d44b-beb4-4424-a803-c6aa28fe4e47`，约 218.44 秒；123 成功、0 失败、0 待完成，无重复 item_key、无序列化警告 |
| 长操作控制 | 超过 30 秒后查询、协作取消、续跑完成；普通回放查询返回 REPLAY_BUSY |
| 状态查询成本 | 该批次 219 次查询，最大约 47 ms；中位低于本机计时分辨率，不解释为零耗时。单条摘要页最大 3588 字节，完整绑定详情通过 details_path 读取 |
| 清单写入期间保活 | 大清单移到后台工作线程后，批次结束经健康探针确认仍为健康 Vulkan 回放 |
| 纹理额度 | 两个 draw、额度 1，进入 TEXTURE_BUDGET 暂停；补充额度后完成，无重复完成条目 |
| 跨加载续跑 | 暂停后重新加载，旧作业续跑明确返回 STALE_JOB |
| 重复请求计数 | 两个相同 draw、两个相同实例，仅导出一个条目；requested=2、valid_draws=1、skipped=1、pending=0 |
| Shader 证据包 | SPIR-V 魔数正确，原始文件 SHA256 与独立原生 ShaderReflection.rawBytes 一致 |
| HDR 数值差分 | R11G11B10_FLOAT，EID 155→1532；512×512 ROI 中像素 (1181,548) 从 `[0,0,0,1]` 到 `[21,23.75,26.5,1]`，有符号差值逐通道与原生 PickPixel 相同 |
| 像素历史 | 原生支持；EID 967 截止的 5 条历史，event／fragment 和 postMod 值逐项一致，分页通过 |
| 查询后的状态 | replay 恢复到 EID 2373，Shader 替换列表保持为空；最终健康探针通过 |

曾出现过原生加载错误和远端断连。这些失败记录保留在本地证据目录，没有把作业的
`completed` 或 mock 结果替代业务验收。状态查询已改为原子磁盘快照；原生停滞期间可查询
阶段和持续时间。不可取消的原生调用仍不会被强行终止。

## 观察记录：原生 post-VS 恒值（不阻塞验收）

EID 169、633、949、961、1942 的采样中，返回了不同的有效顶点引用，但每个 draw 的完整
position.xyzw 均呈恒值。独立原生 `GetPostVSData` + `GetBufferData` 读取与 MCP 完全一致，
原生 `MeshFormat.status` 为空。例：EID 949 的六个引用对应的 xyzw 均为
`[-3.631345510482788,-2.751162052154541,0.00998746883124113,3.764349937438965]`。

**本次验收检查 MCP 是否正确返回 RenderDoc 官方 API 的结果；索引和完整 xyzw 原生对照一致，
因此此项通过。**恒值现象没有被确认为 MCP 缺陷，也不作为本次 P0–P2 修复未完成的依据。
MCP 保留官方返回值，质量诊断继续报告恒值属性、重复率及退化观察。

恒值的具体成因尚未确定；当前对照没有进一步证明 Shader 运算或几何语义是否符合预期，
也不能据此认定“没有落盘”或归咎某个 SWIG／驱动问题。这些问题保留为后续调查方向，
不扩展本次 MCP 原生读取一致性验收的范围。

提供了不依赖 MCP 的 [原生最小复现脚本](../scripts/repro_postvs_native.py)。在已加载此捕获的
RenderDoc Python UI 内运行，输出位于 `%TEMP%/renderdoc_mcp/postvs_native_repro.json`。
它保存实际 MeshFormat、索引和完整 xyzw，最终恢复原事件，可用于后续调查恒值现象的成因。

## 本地证据与复现

`evidence/live_v2/` 已被 Git 忽略，包括请求、响应、CSV、纹理和大数组；未把这些资源加入版本库。
当前工作区保留：

- `final_verification.json`：固定功能、网格／UBO、Shader、像素历史、状态恢复对照。
- `hdr_nonzero_probe.json`：真实 HDR 非零差值及原生像素探针。
- `extra_verification.json`：长批次、远端文件、STALE_JOB 和结束时健康状态。
- `final_boundary_verification.json`：最后计数边界、部署指纹和健康状态。
- `mcp_acceptance.jsonl`、`final_mcp.jsonl`、`extras_mcp.jsonl`：实际请求／响应。
- `native_mesh_*.json`、`native_postvs_probe_633.json`：独立原生 post-VS 证据。
- `bootstrap.py`、`recover.py`、`verify_final.py`、`acceptance.py`、`verify_extras.py`：本次本地验收脚本。

本地重跑需先在 RenderDoc 的 UI Python 环境运行 bootstrap，再按顺序执行 recover、verify_final、
acceptance（`--no-reload` 使用已安装包）、verify_extras。脚本使用明确设备／捕获／EID，
换捕获时必须重新选择事件与资源，不能将这些值移入通用重建指导。
