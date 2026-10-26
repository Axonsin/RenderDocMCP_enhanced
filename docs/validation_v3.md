# RenderDoc MCP 3.0 验收记录

验收日期：2026-10-25。本记录区分自动化验证、真实设备验证及尚未验证的行为。
升级和调用变化见 [migration_v3.md](migration_v3.md)，公开参数见
[tools_zh.md](tools_zh.md) 和 [tool_schemas.json](tool_schemas.json)。

## 版本与部署来源

| 项目 | 本次结果 |
| --- | --- |
| MCP 包 / 扩展 | 3.0.0 / 3.0.0，已成对安装 |
| API 契约 / 文件 IPC | 3 / 2 |
| RenderDoc | 1.46 |
| 扩展语法 | 32 个 Python 文件通过 Python 3.6 AST 检查 |
| 公开工具 | 实际 FastMCP schema 为 45 项 |
| 最终扩展 build hash | `8e5f804c0fdfa6b910e76686c5b5c6425c91b083529054d36f249369f0cd48c6` |
| 回放目标 / API | `adb://HA29QMVJ` / Vulkan |
| 捕获 | `com.Sunborn.SnqxExilium_2026.10.02_22.50_frame3369.rdc` |
| 捕获 SHA-256 | `63fc25ea89e49706a452469bae970b1063526f1f4b93ecf67f4049d2d42eccbb` |

最终运行时报告的扩展 hash 与源目录、安装目录一致。此次未发布版本、创建 Git 标签或推送代码。
安装器保留了扩展回滚备份；重新加载捕获会生成新会话，旧绑定和作业不能跨会话复用。

## 自动化结果

执行命令：

```powershell
python -m pytest tests -q --tb=short --junitxml=evidence/v3/unit_tests.xml
python scripts/check_contracts.py
python skill-support/sync_references.py --check
git diff --check
```

全量回归 **236 passed，92 subtests passed**，无失败或跳过。JUnit 计入子测试后为 328 条记录。
契约检查通过：版本、API/IPC、Python 3.6 语法、实际工具 schema、已发布参数默认值、
文档工具覆盖和共享参考同步均通过；差异空白检查通过。

| 范围 | 自动化覆盖 |
| --- | --- |
| 生命周期和健康 | 远端失联、fatal、API 不一致、操作后失效、恢复事件失败、作业会话失效、首次失效快照 |
| IPC | 临时及永久 PermissionError、有效结果的清理失败、迟到响应、并发客户端、只提交一次 |
| 常量和证据包 | 事件范围、dynamic offset、完整树、数组/矩阵顺序、有符号整数、不可用路径、内容去重及损坏产物拒绝 |
| 纹理 | auto 阈值、inline 超限、文件哈希、布局、D16/D24S8、样本、ROI、sRGB、短读及未知布局拒绝解码 |
| 诊断 | 默认不调用 ADB、白名单、总时限、容量、轮转、设备不可用时保留本机结果 |
| 原有能力 | 管线、资源、网格、shader 编辑、异步作业和取消续跑的既有回归 |

故障路径使用可控模拟；它们不等价于真实驱动故障测试。

## Android 真实冒烟结果

最终构建的证据位于本地 `evidence/v3/release/`。
入口脚本为 [validate_v3_live.py](../scripts/validate_v3_live.py)，汇总见
[report.json](../evidence/v3/release/report.json)，补充逐字节检查见
[additional_artifact_checks.json](../evidence/v3/release/additional_artifact_checks.json)。

| 检查 | 实测结果 |
| --- | --- |
| 打开捕获和共享来源 | 远端打开成功；捕获、导出和作业来源使用同一 capture_session / replay_revision |
| dump_draws | EID 1922、1930 的网格与完整常量作业完成，2 个成功条目、0 个失败、0 个 pending；本次明确关闭该作业的纹理导出 |
| 常量原始字节 | 12 个实际绑定逐一按来源事件、offset、length 独立读取，与导出文件逐字节一致；内容相同的绑定仍分别记录来源 |
| shader bundle | 作业完成，含事件绑定和常量；原始 SPIR-V 文件头验证通过 |
| D16 原始文件 | EID 218，ResourceId::17571，2048×2048、8,388,608 字节；auto 返回文件及布局，不内联大块数据 |
| D16 depth ROI | 16×16 归一化 float32 与原始 16 位值独立解码一致 |
| D24S8 原始文件 | ResourceId::27187，6,665,088 字节；auto 文件返回及哈希、布局检查通过 |
| D24S8 stencil | 指定 MSAA sample 0、1 的 ROI 均成功；sample 0 与原始高 8 位逐像素核对一致 |
| D24S8 depth | EID 2006、sample 0、16×16 ROI 共 256 像素；归一化 float32 与原始低 24 位独立解码一致 |
| stencil 跨事件比较 | EID 1976 → 2006 的指定样本比较作业完成，无隐式 resolve |
| 本机与设备诊断 | 默认本机诊断和显式 ADB 诊断均交付文件、哈希和 manifest；两者 warnings 均为空 |
| 查询恢复 | 结束时 UI/replay 事件仍为 2504，替换列表仍为空，replay_healthy=true |

最终实测会话为 `5454ad7b1e064f3cb718a7440ba66a91`，修订为 0。
大文件哈希及原始来源保存在各请求和产物 sidecar 中；完整常量不进入工具状态页。

补充验证：在 `LoadCapture` 尚未返回、作业处于 `loading_capture` 时，离线诊断约 **13 ms**
返回，随后加载成功并恢复健康状态。证据见
[during_load.json](../evidence/v3/ui_busy/during_load.json)。该补充测量使用前一个候选构建
`eb5c8d…`，离线诊断实现与最终构建相同；它不作为最终构建的独立性能基准。
升级过程中，3.0 服务访问旧扩展曾实际得到 `API_VERSION_MISMATCH`，见
[predeploy_mismatch.json](../evidence/v3/predeploy_mismatch.json)。

## 边界与未验证项

- 本次未观察到新的自然断连，也未主动杀进程、拔设备或制造驱动故障。
  因此真实断连后的拒绝、首次失效取证和人工恢复仍待现场验证；不能据此认定此前断连的根因。
- 真实设备验证覆盖当前 Android Vulkan 捕获。D3D11/D3D12、其他驱动和 OpenGL 的真实数据布局
  未在本轮设备上验证；不具备已验证布局时仅保留 opaque 原始字节，拒绝猜测 aspect/ROI 数值。
- 首批 depth/stencil 数值支持限 D16、D24S8。其他深度格式的原始导出不代表支持数值解码。
- 原生调用未返回时只能报告进行中或结果未知，不能强制取消，也不自动重提业务操作。
- Python 3.6 兼容性使用语法检查并结合 RenderDoc 1.46 实测；未另行启动独立 Python 3.6 解释器。
- 上述设备产物及日志位于本机被忽略的 `evidence/` 目录，未默认纳入 Git；分享前需显式打包该目录。

核心四项增强、成对部署及当前捕获冒烟通过。未验证行为按上述边界保留，不用模拟结果替代设备结论。
