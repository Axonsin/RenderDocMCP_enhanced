# SS TrainStage benchmark tooling

本目录归档本次测评建设的可复用评分工具、合成测试、四类任务和12道基础题。数据版本为0.1.0-rc1，协议为rdoc-ss-frame2925-v2。

RDC、游戏资产、私有答案、参考工程和实际取证日志不随仓库分发。完整私有包仍在制作机器的RenderDocBenchmark目录；需要授权捕获才能执行公开任务。dataset/case.json中的冻结状态描述该本地参考快照，不代表这个源码子集包含完整数据或已具备正式被测隔离环境。

运行：

```powershell
python -m pip install -r harness/requirements.txt
python -m unittest discover -s harness/tests -v
```

导入、评审及Markdown报告命令见harness/README.md。文档中oracle/reference/已有测试结果等路径指完整私有包，不在此仓库中。export_public需要自行提供与dataset/case.json哈希一致且获授权使用的RDC；它不下载捕获。LPIPS依赖与权重需单独准备，不会用随机权重替代。

本仓库保留92项可独立运行的工具测试；私有包另有2项依赖Blender参考脚本的测试，不随本目录分发。没有模型成绩或排名。

实测故障及当前源码核对见[工具问题记录](TOOL_FINDINGS.md)。这次提交归档评测实现，没有修改RenderDoc服务实现。
