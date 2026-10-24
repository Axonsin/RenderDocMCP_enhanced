# 长程重建期间的工具问题

核对日期：2026-10-24。捕获取证使用RenderDoc1.46和已安装的旧扩展1.0.1a1；当时运行接口仍是get_draw_calls/event_id，而仓库已使用get_actions/action_event_id。旧运行结果不能直接当作当前源码版本的实机测试结论。以下源码核对基于6776507ef81d8bb641b4c44295185e32a959f1d2，本次未修复服务代码。

| 优先级 | 问题与影响 | 当前核对 |
|---|---|---|
| P0 | 断连后曾返回空常量或错误API的占位状态；480片元导出带driver-not-loaded且变量树全空，重建器误用零值导致黑墙 | 运行中真实发生。需端到端健康/数据完整性检查，不能仅凭文件存在或transport success接受答案；新版本尚未重新实测 |
| P1 | SNorm8解码错误，影响法线和packed属性 | 当前mesh_service.py仍使用129作分母，最负值还直接返回-128；应按有符号归一化语义处理，而非当前结果 |
| P1 | VSOut导出报MeshFormat无name，且旧响应success=false/error=null | 当前GetPostVSData返回对象后，下游仍直接读取mesh.name；源码风险仍在，需匹配反射输出签名，并保留真实异常 |
| P1 | Mesh实例覆盖不足 | 当前VSIn跳过perInstance属性；GetPostVSData固定instance0，缺乏逐实例选择。裁判实际依靠原生逐实例导出补齐，纯MCP赛道不能暗中这样补齐 |
| P1 | 查询污染隐藏replay位置，UI事件却不变 | 旧facade实测2194查询232后shader状态停在232。当前pipeline/resource已使用finally恢复的at_event，但mesh服务仍直接SetFrameEvent，需统一核查 |
| P1 | 整数常量缺值 | 旧解码遗漏实例参数和25处VFX整数。当前shader_variables.py已有Int/UInt/Bool映射，不能声称新版本仍全数缺失；需部署后对整数、数组、嵌套块回归 |
| P2 | IPC响应非原子写入曾引发读失败 | 当前源码已有os.replace和跨客户端事务锁；属于已有改进、运行扩展未同步验证，不能重复记为当前已证实缺陷 |
| P2 | 纹理导出成功不等于数据可用或颜色语义明确 | 相机深度2340导出全零，不能用作真值；部分sRGB资源导出的PNG已经是解码数值，再解码导致变暗。建议明确导出域、子资源、有效性与诊断；全零本身不总是错误 |

## 环境问题与能力边界

- 本次ADB断连已定位到我们启动的Unity批处理退出日志中的Killing ADB server，不应归因于用户或直接认定MCP故障。之后串行操作；用户断开实机后不再使用ADB。
- Local回放已获用户授权，但本次未由裁判完成新的健康验收。后续Local与原远端GPU时间不可混算。
- GPU counter只取得一次回放样本，不能据此宣称原游戏瓶颈或优化收益；单帧无法证明缓存淘汰等跨帧机制。
- 建议首先提供明确的运行版本/协议/回放健康信息，再修复mesh解码、PostVS属性和逐实例读取，最后覆盖所有查询的状态恢复与失败响应。
- 正式评测还需要隔离所有工具后端，包括Blender MCP的Python执行。当前裁判宿主能读取源码和答案，不能直接作为候选沙箱。

私有依据位于完整测评包的oracle/evidence/environment.json、state_restore_probe.json、shader_integrity_audit.json、lighting/depth_validation.json及Unity构建日志；这些游戏取证数据不上传此仓库。
