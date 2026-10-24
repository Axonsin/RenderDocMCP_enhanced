# 长程重建期间的工具问题

核对日期：2026-10-24。捕获取证使用RenderDoc1.46和已安装的旧扩展1.0.1a1；当时运行接口仍是get_draw_calls/event_id，而仓库已使用get_actions/action_event_id。旧运行结果不能直接当作当前源码版本的实机测试结论。以下源码核对基于6776507ef81d8bb641b4c44295185e32a959f1d2。

2026-10-24更新：按下方核对结论完成一轮源码修复（版本/协议/回放健康上报、mesh解码与PostVS签名、逐实例参数、全部查询的异常隔离与replay位置恢复、纹理导出诊断），扩展单元测试扩充至116项。修复经Codex四轮对抗审查收敛至无新增问题（期间修正了post-VS布局规则、stream选择、实例寻址公式、64位整数解码等复审发现）。除IPC项外各行"当前核对"已更新为修复后状态；所有修复仍待实机（RenderDoc真实捕获）重测确认。

| 优先级 | 问题与影响 | 当前核对 |
|---|---|---|
| P0 | 断连后曾返回空常量或错误API的占位状态；480片元导出带driver-not-loaded且变量树全空，重建器误用零值导致黑墙 | 运行中真实发生。源码已修：get_capture_status/ping 返回扩展/RenderDoc/IPC版本与 replay 健康探针（GetAPIProperties+GetFatalErrorStatus）；get_actions/get_frame_summary/get_action_timings/get_buffer_contents/mesh 工具回调补齐异常隔离，失败显式报稳定错误码。需实机断连重测验证探针有效 |
| P1 | SNorm8解码错误，影响法线和packed属性 | 已修复：SNorm 按 2^(bits-1)-1 归一化（8位分母127），最负值映射为-1.0；附SNorm8/16单测 |
| P1 | VSOut导出报MeshFormat无name，且旧响应success=false/error=null | 已修复：VSOut/GSOut 属性来自 shader 输出签名（semanticIdxName 命名），布局按原生网格查看器规则计算——按光栅化 stream 过滤（VSOut 固定 stream 0）、Position 提前、分量 32 位展开、仅 HasAlignedPostVSData 时 vec4 对齐，并用 vertexByteStride 校验；GSOut 阶段按实际绑定判断（Geometry/Domain）；不再读 GetPostVSData 的 mesh.name；签名或布局提示缺失报 MESH_SIGNATURE_UNAVAILABLE；mesh 三工具回调经 at_event 异常隔离。需实机验证各后端 |
| P1 | Mesh实例覆盖不足 | 已修复：VSIn 不再跳过 perInstance 属性，寻址按原生规则（instanceOffset 平移读窗、rate 仅除 0-based instance、rate 0 恒读 element 0），GetPostVSData 按 instance 选择；get_mesh_summary/get_mesh_data/export_mesh_csv 新增 instance 参数（默认0，超界报 INVALID_INSTANCE）。需实机逐实例验证 |
| P1 | 查询污染隐藏replay位置，UI事件却不变 | 已修复：mesh 三工具、get_action_details、trace_action_dependencies 改用 at_event（finally 恢复）；search_actions/analyze_pass 扫描循环保存 CurEvent 并 finally 恢复，全部扫描失败时报 RESOURCE_QUERY_FAILED 而非空结果 |
| P1 | 整数常量缺值 | 源码确认 shader_variables.py 已有 Int/UInt/Bool/SShort 等映射及数组、嵌套块解码；本轮补整数/布尔/嵌套回归单测。部署后仍需对实机 cbuffer 回归 |
| P2 | IPC响应非原子写入曾引发读失败 | 当前源码已有 os.replace 原子写与 _busy 互斥（注：_busy 是单 RenderDoc 实例内的进程互斥，不是跨客户端文件锁）；本轮未改动 |
| P2 | 纹理导出成功不等于数据可用或颜色语义明确 | 已补诊断：get_texture_data 返回 color_space/all_zero/warnings（0字节与全零分别提示）；save_texture 未知 format_type/alpha_mode 报 INVALID_FORMAT_TYPE/INVALID_ALPHA_MODE（不再静默回退），mip=-1 响应带 mip_selection；sRGB 导出语义已写入文档。相机深度等实机有效性验证仍待做 |

## 环境问题与能力边界

- 本次ADB断连已定位到我们启动的Unity批处理退出日志中的Killing ADB server，不应归因于用户或直接认定MCP故障。之后串行操作；用户断开实机后不再使用ADB。
- Local回放已获用户授权，但本次未由裁判完成新的健康验收。后续Local与原远端GPU时间不可混算。
- GPU counter只取得一次回放样本，不能据此宣称原游戏瓶颈或优化收益；单帧无法证明缓存淘汰等跨帧机制。
- 原建议的三个阶段（版本/协议/回放健康信息 → mesh解码、PostVS属性和逐实例读取 → 全部查询的状态恢复与失败响应）已在源码层面完成；下一步是在真实捕获上重测，确认签名偏移、逐实例数据与健康探针在断连场景下的表现。
- 正式评测还需要隔离所有工具后端，包括Blender MCP的Python执行。当前裁判宿主能读取源码和答案，不能直接作为候选沙箱。

私有依据位于完整测评包的oracle/evidence/environment.json、state_restore_probe.json、shader_integrity_audit.json、lighting/depth_validation.json及Unity构建日志；这些游戏取证数据不上传此仓库。
