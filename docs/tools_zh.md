# MCP 工具参考

所有 RenderDoc MCP 工具的详细参考文档，包含参数、返回值和使用示例。

[English](tools.md)

## 推荐流程

一个典型的分析流程通常遵循以下模式：

`get_capture_status` / `get_frame_summary` -> `get_draw_calls` / `search_draws` -> `get_pipeline_state` / `get_shader_info` / `get_mesh_data`

---

## 全局操作能力

### 捕获管理

#### `open_capture`

打开 RenderDoc 捕获文件 (.rdc)。会自动关闭当前已打开的捕获。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `capture_path` | `str` | 是 | 捕获文件的完整路径 |

**返回值：** `{"success": true, "filename": "game.rdc", "api": "D3D11"}`

**示例：**
```
open_capture(capture_path="D:/captures/game.rdc")
```

---

#### `list_captures`

列出目录中所有 `.rdc` 文件。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `directory` | `str` | 是 | 要搜索的目录路径 |

**返回值：** 包含 `filename`、`path`、`size_bytes`、`modified_time` 的列表。

**示例：**
```
list_captures(directory="D:/captures")
# → {"count": 3, "captures": [{"filename": "game.rdc", "path": "D:/captures/game.rdc", "size_bytes": 12345, "modified_time": "..."}]}
```

---

#### `get_capture_status`

检查 RenderDoc 中是否已加载捕获。如果已加载则返回捕获状态和 API 类型。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| *(无)* | | | |

**返回值：** `{"loaded": true, "api": "D3D11"}` 或 `{"loaded": false}`

**示例：**
```
get_capture_status()
```

---

### 帧概览

#### `get_frame_summary`

获取整帧统计信息和顶层 marker 摘要。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| *(无)* | | | |

**返回值：** API 类型、action 总数、统计信息（draw calls、dispatches、clears、copies、presents、markers）、顶层 marker（含 event ID 和子级数量）、资源数量（纹理、缓冲区）。

**示例：**
```
get_frame_summary()
```

---

#### `summarize_capture`

在 `get_frame_summary` 之上额外获取全帧 GPU 时间并进行排序去重，返回高层概览与建议的分析入口。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| *(无)* | | | |

**返回值：** 帧统计信息、`hot_actions`（GPU 时间 Top 10）、主要 marker、`suggested_entry_points`。

**示例：**
```
summarize_capture()
```

---

### Action 导航

#### `get_draw_calls`

获取 draw call 和 action 的层级结构，支持过滤。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `include_children` | `bool` | 否 | `true` | 包含子级 action |
| `marker_filter` | `str` | 否 | | 仅包含标记路径中包含此字符串的 action（部分匹配） |
| `exclude_markers` | `list[str]` | 否 | | 排除标记路径中包含这些字符串的 action |
| `event_id_range` | `dict` | 否 | | event ID 范围，格式为 `{"min": ..., "max": ...}` |
| `event_id_min` | `int` | 否 | | event ID 范围下界的旧版别名 |
| `event_id_max` | `int` | 否 | | event ID 范围上界的旧版别名 |
| `only_actions` | `bool` | 否 | `false` | 为 true 时排除 marker action |
| `flags_filter` | `list[str]` | 否 | | 仅包含具有这些标志的 action（如 `["Drawcall", "Dispatch"]`） |

**返回值：** 包含 marker、draw call、dispatch 和其他 GPU 事件的层级树结构。

**示例：**
```
# 获取所有 draw call 及其子级
get_draw_calls(include_children=true)

# 按 marker 和 event 范围过滤
get_draw_calls(marker_filter="Camera.Render", event_id_min=7372, event_id_max=7600)

# 仅 draw call，排除 marker
get_draw_calls(only_actions=true, flags_filter=["Drawcall"])

# 排除特定 marker
get_draw_calls(exclude_markers=["GUI.Repaint", "UIR.DrawChain"])
```

---

#### `search_draws`

按 shader、texture 或 resource 统一搜索 draw call。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `by` | `"shader"` / `"texture"` / `"resource"` | 是 | 搜索模式 |
| `query` | `str` | 是 | shader 名称、纹理名称或 resource ID |
| `stage` | `str` | 否 | shader 阶段过滤（`"vertex"`、`"pixel"`、`"compute"` 等）— 仅在 `by="shader"` 时有效 |

**返回值：** `{"matches": [...], "total_matches": 3, "scanned_count": 150}`

**示例：**
```
search_draws(by="shader", query="Toon", stage="pixel")
search_draws(by="texture", query="CharacterSkin")
search_draws(by="resource", query="ResourceId::12345")
```

---

### 资源空间浏览

#### `list_resources`

使用统一的分页接口列出 texture 或 buffer。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `resource_type` | `"texture"` / `"buffer"` | 是 | | 要列出的资源类型 |
| `name_filter` | `str` | 否 | | 名称部分匹配（不区分大小写） |
| `offset` | `int` | 否 | `0` | 分页起始索引 |
| `limit` | `int` | 否 | `50` | 最大返回资源数 |

**返回值：** `{"items": [...], "total_count": 150, "offset": 0, "limit": 50, "returned_count": 50}`

**示例：**
```
# 按名称过滤列出纹理
list_resources(resource_type="texture", name_filter="Scene", offset=0, limit=50)

# 列出缓冲区
list_resources(resource_type="buffer", name_filter="Camera", offset=0, limit=50)

# 分页访问
list_resources(resource_type="texture", offset=50, limit=50)
```

---

## 局部数据分析能力

### Pipeline 状态

#### `get_pipeline_state`

获取指定 event 处的完整图形管线状态。包含绑定的 shader、资源绑定、采样器、常量缓冲区、渲染目标、输入/输出纹理摘要、视口和输入装配状态。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `event_id` | `int` | 是 | 要检查的 event ID |

**返回值：** 完整管线状态，含 `input_textures` / `output_textures` 摘要。

**示例：**
```
get_pipeline_state(event_id=123)
# → { ..., "input_textures": [{"resource_id": "ResourceId::2495", "name": "CharacterDiffuse", ...}],
#        "output_textures": [{"resource_id": "ResourceId::3001", "type": "render_target", ...}],
#        "input_count": 3, "output_count": 2 }
```

---

#### `get_shader_info`

获取指定 event 处特定阶段的 shader 信息。包含反汇编代码、常量缓冲区值和资源绑定。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `event_id` | `int` | 是 | event ID |
| `stage` | `str` | 是 | shader 阶段：`"vertex"`、`"hull"`、`"domain"`、`"geometry"`、`"pixel"`、`"compute"` |

**返回值：** shader resource ID、入口点、阶段、反汇编、常量缓冲区、资源绑定。

**示例：**
```
get_shader_info(event_id=123, stage="pixel")
```

---

### 资源数据读取

#### `get_texture_info`

获取纹理资源的元数据。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `resource_id` | `str` | 是 | 资源 ID（如 `"ResourceId::2495"`） |

**返回值：** 尺寸、格式、mip 级别、数组大小等属性。

**示例：**
```
get_texture_info(resource_id="ResourceId::2495")
```

---

#### `get_texture_data`

读取纹理资源的像素数据。返回 Base64 编码的字节。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `resource_id` | `str` | 是 | | 资源 ID |
| `mip` | `int` | 否 | `0` | 要获取的 mip 级别 |
| `slice` | `int` | 否 | `0` | 数组切片或立方体贴图面索引（0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-） |
| `sample` | `int` | 否 | `0` | MSAA 采样索引 |
| `depth_slice` | `int` | 否 | | 仅限 3D 纹理，提取特定深度切片。省略时返回完整体积。 |

**返回值：** Base64 编码的像素数据，含元数据（尺寸、格式）。

**示例：**
```
# 获取 2D 纹理的 mip 0
get_texture_data(resource_id="ResourceId::123")

# 获取特定的 mip 级别
get_texture_data(resource_id="ResourceId::123", mip=2)

# 获取立方体贴图的特定面 (0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-)
get_texture_data(resource_id="ResourceId::456", slice=3)

# 获取 3D 纹理的特定深度切片
get_texture_data(resource_id="ResourceId::789", depth_slice=5)
```

---

#### `get_buffer_contents`

读取缓冲区资源的内容。返回 Base64 编码的字节。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `resource_id` | `str` | 是 | | 资源 ID |
| `offset` | `int` | 否 | `0` | 开始读取的字节偏移量 |
| `length` | `int` | 否 | `0` | 要读取的字节数（0 = 整个缓冲区） |

**返回值：** Base64 编码的缓冲区数据，含元数据。

**示例：**
```
# 获取整个缓冲区
get_buffer_contents(resource_id="ResourceId::123")

# 从偏移量 256 获取 512 字节
get_buffer_contents(resource_id="ResourceId::123", offset=256, length=512)
```

---

#### `get_mesh_summary`

获取特定 draw call 事件的网格数据摘要。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `event_id` | `int` | 是 | draw call 的 event ID |

**返回值：** 拓扑结构、顶点/索引数量、是否使用索引缓冲、顶点属性及其格式、包围盒。

**示例：**
```
get_mesh_summary(event_id=1234)
# → {"topology": "TriangleList", "num_vertices": 3024, "num_indices": 9072, "indexed": true,
#    "attributes": [{"name": "POSITION", "format": "R32G32B32_FLOAT", "components": 3}, ...],
#    "bounding_box": {"min": [-10.0, -5.0, -2.0], "max": [10.0, 5.0, 2.0]}}
```

---

#### `get_mesh_data`

获取特定 draw call 的网格顶点和索引数据，支持分页。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `event_id` | `int` | 是 | | event ID |
| `stage` | `str` | 否 | `"VSIn"` | 网格数据阶段：`"VSIn"`（输入）、`"VSOut"`（顶点着色器输出）、`"GSOut"`（几何着色器输出） |
| `offset` | `int` | 否 | `0` | 分页起始顶点偏移量 |
| `limit` | `int` | 否 | `100` | 最大返回顶点数（建议：100-500） |
| `start_offset` | `int` | 否 | `0` | `offset` 的旧版别名 |
| `max_vertices` | `int` | 否 | `100` | `limit` 的旧版别名 |
| `attributes` | `list[str]` | 否 | | 过滤特定属性名称（如 `["POSITION", "NORMAL"]`）。省略时包含所有属性。 |

**返回值：** `vertices`、`indices`、`topology`、`attribute_info`、`total_count`、`has_more`、`truncated`。

**示例：**
```
# 第一页
get_mesh_data(event_id=1234, offset=0, limit=100)

# 下一页
get_mesh_data(event_id=1234, offset=100, limit=100)

# 过滤特定属性
get_mesh_data(event_id=1234, offset=0, limit=100, attributes=["POSITION", "NORMAL", "TEXCOORD"])
```

---

### Action 元信息

#### `get_draw_call_details`

获取特定 draw call 的详细信息。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `event_id` | `int` | 是 | draw call 的 event ID |

**返回值：** 顶点/索引数量、资源输出和其他元数据。

**示例：**
```
get_draw_call_details(event_id=123)
```

---

#### `get_action_timings`

获取 action 的 GPU 时间信息。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `event_ids` | `list[int]` | 否 | | 指定的 event ID 列表。省略时返回所有 action。 |
| `marker_filter` | `str` | 否 | | 仅包含标记路径中包含此字符串的 action |
| `exclude_markers` | `list[str]` | 否 | | 排除标记路径中包含这些字符串的 action |

**返回值：** `{"available": true, "unit": "CounterUnit.Seconds", "timings": [...], "total_duration_ms": 12.5, "count": 150}`

> **注意：** GPU 时间计数器在某些硬件/驱动上可能不可用。如果 `available` 为 `false`，则无法获取时间数据。

**示例：**
```
# 所有 action
get_action_timings()

# 指定 event ID
get_action_timings(event_ids=[100, 200, 300])

# 按 marker 过滤
get_action_timings(marker_filter="Camera.Render", exclude_markers=["GUI.Repaint"])
```

---

### 组合分析

在原子工具之上编排多个服务的跨维度复合查询，帮助快速获得全局视图。

#### `inspect_event`

对单个 event 做复合检查，返回紧凑的详情、时间、shader 摘要、管线摘要与网格摘要。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `event_id` | `int` | 是 | 要检查的 event ID |

**返回值：** event 详情、时间、shader 摘要、管线摘要、网格摘要。

**示例：**
```
inspect_event(event_id=1517)
```

---

#### `trace_resource_usage`

追踪资源在匹配事件中的读取、写入与消费过程。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `resource_id` | `str` | 是 | | 要追踪的资源 |
| `marker_filter` | `str` | 否 | | marker 路径子串过滤 |
| `exclude_markers` | `list[str]` | 否 | | 要排除的 marker 子串 |
| `event_id_range` | `dict` | 否 | | event 范围，格式为 `{"min": ..., "max": ...}` |
| `event_id_min` | `int` | 否 | | event 范围下界的旧版别名 |
| `event_id_max` | `int` | 否 | | event 范围上界的旧版别名 |
| `before_event_id` | `int` | 否 | | 计算此 event 之前的最近写入者 |

**返回值：** 资源元数据、使用角色、读/写事件列表、写入者摘要。

**示例：**
```
trace_resource_usage(resource_id="ResourceId::2495")
trace_resource_usage(resource_id="ResourceId::2495", marker_filter="Forward", before_event_id=1517)
```

---

#### `trace_event_dependencies`

追踪单个 event 的直接资源依赖。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `event_id` | `int` | 是 | 要检查的 event |

**返回值：** 按阶段分组的输入资源、输入装配缓冲区、输出资源、主要输入的候选 producer event。

**示例：**
```
trace_event_dependencies(event_id=1517)
```

---

#### `diff_events`

对比两个 event，突出关键状态差异。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `event_id_a` | `int` | 是 | 第一个 event ID |
| `event_id_b` | `int` | 是 | 第二个 event ID |

**返回值：** shader、资源绑定、绘制参数、网格和时间差异。

**示例：**
```
diff_events(event_id_a=100, event_id_b=200)
```

---

#### `analyze_pass`

将一个 marker 子树或 pass 汇总为一个整体工作负载。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `marker_filter` | `str` | 是 | | marker 路径子串，用于选择 pass 子树 |
| `exclude_markers` | `list[str]` | 否 | | 要排除的 marker 子串 |

**返回值：** action 数量、主要 shader、代表性资源、耗时最高的 action、保守的工作负载警告。

**示例：**
```
analyze_pass(marker_filter="ShadowPass")
analyze_pass(marker_filter="Forward", exclude_markers=["GUI"])
```

---

## 上层工具能力

### 资源导出

#### `save_texture`

将纹理保存为图片文件。自动处理格式转换。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `resource_id` | `str` | 是 | | 资源 ID（如 `"ResourceId::2495"`） |
| `output_path` | `str` | 是 | | 输出文件路径（如 `"D:/output/texture.png"`） |
| `format_type` | `str` | 否 | `"PNG"` | 输出格式：`"PNG"`、`"JPG"`、`"BMP"`、`"TGA"`、`"EXR"`、`"DDS"`、`"HDR"` |
| `mip` | `int` | 否 | `0` | 要保存的 mip 级别（`-1` = 所有 mip） |
| `slice_index` | `int` | 否 | `0` | 数组切片或立方体贴图面索引（0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-） |
| `alpha_mode` | `str` | 否 | `"preserve"` | Alpha 处理：`"preserve"`、`"discard"`、`"blend_to_black"` |

**返回值：** `{"success": true, "dimensions": [1920, 1080], "output_path": "D:/output/texture.png"}`

**示例：**
```
# 保存为 PNG
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.png")

# 保存为 JPG，alpha 混合到黑色背景
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.jpg", format_type="JPG", alpha_mode="blend_to_black")

# 导出所有 mip 级别为 DDS
save_texture(resource_id="ResourceId::2495", output_path="D:/output/texture.dds", format_type="DDS", mip=-1)
```

---

#### `export_mesh_csv`

将网格数据导出为 CSV 文件，与 [csv_obj](https://github.com/nicbarker/csv_obj) 项目兼容。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `event_id` | `int` | 是 | | draw call 的 event ID |
| `output_path` | `str` | 是 | | 输出文件路径（如 `"D:/output/mesh.csv"`） |
| `stage` | `str` | 否 | `"VSIn"` | 网格数据阶段：`"VSIn"`、`"VSOut"`、`"GSOut"` |
| `include_attributes` | `list[str]` | 否 | | 过滤特定属性。省略时包含所有属性。 |

**返回值：** `{"success": true, "output_path": "D:/output/mesh.csv", "index_path": "D:/output/mesh.idx", "vertex_count": 3024, "index_count": 9072}`

**CSV 格式说明：**
- 第一行：`VTX,IDX,in_POSITION0.x,in_POSITION0.y,...`
- VTX：去重后的顶点索引
- IDX：原始顶点索引
- 索引 sidecar 文件（`.idx`）：重映射后的三角形流

**示例：**
```
export_mesh_csv(event_id=1234, output_path="D:/output/mesh.csv", stage="VSIn", include_attributes=["POSITION", "NORMAL", "TEXCOORD"])
```
