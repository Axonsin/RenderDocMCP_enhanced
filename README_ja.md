# RenderDoc MCP Server

[English](README.md) | [中文](README_zh.md)

RenderDoc UI拡張機能として動作するMCPサーバー。AIアシスタントがRenderDocのキャプチャデータにアクセスし、グラフィックスデバッグを支援する。

## アーキテクチャ

```
Claude/AI Client (stdio)
        │
        ▼
MCP Server Process (Python + FastMCP 2.0)
        │ File-based IPC (%TEMP%/renderdoc_mcp/)
        ▼
RenderDoc Process (Extension)
```

RenderDoc内蔵のPythonにはsocketモジュールがないため、ファイルベースのIPCで通信を行う。

## セットアップ

### 1. RenderDoc拡張機能のインストール

```bash
python scripts/install_extension.py
```

拡張機能は `%APPDATA%\qrenderdoc\extensions\renderdoc_mcp_bridge` にインストールされる。

### 2. RenderDocで拡張機能を有効化

1. RenderDocを起動
2. Tools > Manage Extensions
3. "RenderDoc MCP Bridge" を有効化

### 3. MCPサーバーのインストール

```bash
uv tool install . # 現在のディレクトリからインストール
uv tool update-shell  # PATHに追加
```

シェルを再起動すると `renderdoc-mcp` コマンドが使えるようになる。

> **Note**: `--editable` を付けると、ソースコードの変更が即座に反映される（開発時に便利）。
> 安定版としてインストールする場合は `uv tool install .` を使用。

### 4. MCPクライアントの設定

#### Claude Desktop

`claude_desktop_config.json` に追加:

```json
{
  "mcpServers": {
    "renderdoc": {
      "command": "renderdoc-mcp"
    }
  }
}
```

#### Claude Code

`.mcp.json` に追加:

```json
{
  "mcpServers": {
    "renderdoc": {
      "command": "renderdoc-mcp"
    }
  }
}
```
>このディレクトリを作業フォルダとして Claude Code を開くこともできます（このディレクトリでターミナルを開き、claude コマンドを実行するのと同じ動作です）。Claude Code は .mcp.json を自動的に検出し、このセッション限りで MCP サーバーを登録します。

## 使い方

1. RenderDocを起動し、キャプチャファイル (.rdc) を開く
2. MCPクライアント (Claude等) から RenderDoc のデータにアクセス

## MCPツール一覧

### コア解析ツール

- `get_capture_status` - キャプチャの読み込み状態を確認
- `get_draw_calls` - draw call / action の階層をフィルタ付きで取得
- `get_frame_summary` - フレーム全体の統計とトップレベル marker を取得
- `get_draw_call_details` - 特定 draw call の詳細情報を取得
- `get_action_timings` - action の GPU 時間を取得
- `get_shader_info` - shader 逆アセンブル、定数バッファ、バインディングを取得
- `get_pipeline_state` - 完全なパイプライン状態と簡潔な入出力テクスチャ要約を取得
- `get_mesh_summary` - メッシュのトポロジ、件数、属性、境界を取得
- `get_mesh_data` - メッシュデータをページング取得

### Canonical な検索・リソースツール

- `search_draws` - shader / texture / resource で draw call を統一検索
- `list_resources` - texture と buffer を 1 つのページング API で列挙
- `get_texture_info` - テクスチャのメタデータを取得
- `get_texture_data` - テクスチャのピクセルデータを取得 (Base64)
- `get_buffer_contents` - バッファ内容を取得 (Base64)
- `save_texture` - テクスチャを画像ファイルに保存 (PNG/JPG/BMP/TGA/EXR/DDS/HDR)

### ワークフロー / 高度なツール

- `open_capture` - MCP クライアントからキャプチャを開く
- `list_captures` - ディレクトリ内の `.rdc` ファイルを列挙
- `export_mesh_csv` - 下流ワークフロー向けにメッシュ CSV を出力

## 使用例

### draw call の統一検索

```
search_draws(by="shader", query="Toon", stage="pixel")
search_draws(by="texture", query="CharacterSkin")
search_draws(by="resource", query="ResourceId::12345")
```

### リソースの統一列挙

```
list_resources(resource_type="texture", name_filter="Scene", offset=0, limit=50)
list_resources(resource_type="buffer", name_filter="Camera", offset=0, limit=50)
```

### ドローコール一覧の取得

```
get_draw_calls(include_children=true)
```

### シェーダー情報の取得

```
get_shader_info(event_id=123, stage="pixel")
```

### パイプライン状態の取得

```
get_pipeline_state(event_id=123)
```

`get_pipeline_state` の結果には簡潔な `input_textures` / `output_textures` 要約が含まれます。

### canonical なページングでメッシュ取得

```
get_mesh_data(event_id=1234, offset=0, limit=100)
get_mesh_data(event_id=1234, offset=100, limit=100)
```

### テクスチャデータの取得

```
# 2Dテクスチャのmip 0を取得
get_texture_data(resource_id="ResourceId::123")

# 特定のmipレベルを取得
get_texture_data(resource_id="ResourceId::123", mip=2)

# キューブマップの特定の面を取得 (0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-)
get_texture_data(resource_id="ResourceId::456", slice=3)

# 3Dテクスチャの特定の深度スライスを取得
get_texture_data(resource_id="ResourceId::789", depth_slice=5)
```

### バッファデータの部分取得

```
# バッファ全体を取得
get_buffer_contents(resource_id="ResourceId::123")

# オフセット256から512バイト取得
get_buffer_contents(resource_id="ResourceId::123", offset=256, length=512)
```

### テクスチャをファイルに保存

```
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.png")
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.jpg", format_type="JPG")
```

## 要件

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- RenderDoc 1.20+

> **Note**: 動作確認はWindows + DirectX 11環境でのみ行っています。
> Linux/macOS + Vulkan/OpenGL環境でも動作する可能性がありますが、未検証です。

## ライセンス

MIT
