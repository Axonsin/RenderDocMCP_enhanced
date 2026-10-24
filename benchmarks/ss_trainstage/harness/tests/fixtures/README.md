# 非官方合成 fixture

`pipeline_submission` 仅演示工具输入格式。捕获哈希、模型名称和内容均为占位值，不是 SS 捕获的实际结果，不得混入正式运行统计。可以执行：

```powershell
python harness/benchmark.py validate harness/tests/fixtures/pipeline_submission
```

它没有外部评审，不应有任务分数、通过状态或模型排名。测试中的重建文件只具有识别头，也不代表真实可重开的 Blender 工程。
