# RenderDoc MCP Server Enhanced

[English](README.md) | [日本語](README_ja.md) | [中文](README_zh.md)

> これは [RenderDocMCP](https://github.com/halby24/RenderDocMCP) のフォークで、クロス API 互換性（特に OpenGL シーン）と MCP ツールインターフェースの設計改善に重点を置いています。

RenderDoc MCP Enhanced により、AI アシスタントは RenderDoc キャプチャデータに基づいてより効率的なグラフィックスデバッグ、レンダリング分析、最適化提案を行うことができます。

![img.png](docs/images/preview.png)

## アーキテクチャ

本プロジェクトは FastMCP 2.0 ベースのプロセス分離アーキテクチャを採用しています。

`uv` がグローバルコマンド `renderdoc-mcp` を登録します。AI クライアント（Claude など）がこの MCP コマンドを検出すると、MCP Server を起動します。

MCP Server は AI クライアントと stdio 経由で通信し、ファイルベース IPC 経由で RenderDoc 内蔵 Python 3.6 環境で動作する拡張機能にリクエストを転送します。

```
Claude/AI Client (stdio)
        │
        ▼
MCP Server Process (Python + FastMCP 2.0)
        │ File-based IPC (%TEMP%/renderdoc_mcp/)
        ▼
RenderDoc Process (Extension)
```

RenderDoc 内蔵の Python には socket モジュールがないため、ファイルベースの IPC で通信を行います。

## セットアップ

### システム要件

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- RenderDoc 1.20+
- Windows

> **注意**: 現在は Windows 環境でのみテスト済みです。
> 理論上は Linux でも動作する可能性がありますが、テストと適応は行っていません。

### 1. RenderDoc 拡張機能のインストール

リポジトリをクローン後、プロジェクトルートで実行：
```bash
python scripts/install_extension.py
```
拡張機能は `%APPDATA%\qrenderdoc\extensions\renderdoc_mcp_bridge` にインストールされます。

### 2. RenderDoc で拡張機能を有効化

1. RenderDoc を起動
2. Tools > Manage Extensions
3. "RenderDoc MCP Bridge" を有効化

### 3. MCP サーバーのインストール

プロジェクトルートで実行：
```bash
uv tool install . # 現在のディレクトリからインストール
uv tool update-shell  # PATH に renderdoc-mcp を追加
```

シェルを再起動すると `renderdoc-mcp` コマンドが使えるようになります。

> **注意**: `--editable` を付けると、ソースコードの変更が即座に反映されます（開発時に便利）。
> 安定版としてインストールする場合は `uv tool install .` を使用。

### 4. MCP クライアントの設定

#### Claude Desktop

`claude_desktop_config.json` に追加：

```json
{
  "mcpServers": {
    "renderdoc": {
      "command": "renderdoc-mcp"
    }
  }
}
```

#### Claude Code / その他の MCP 対応クライアント

`.mcp.json` に追加：

```json
{
  "mcpServers": {
    "renderdoc": {
      "command": "renderdoc-mcp"
    }
  }
}
```

このプロジェクトディレクトリで直接 Claude Code を起動することもできます。Claude Code は `.mcp.json` を自動的に検出し、現在のセッションで MCP サーバーを登録します。

プロジェクトレベルの設定を使用することをお勧めします。グローバル MCP 設定が他のワークスペースのコンテキストに影響するのを防ぐためです。

![claudeprojectmcp.gif](docs/images/claudeprojectmcp.gif)

## 使い方

1. RenderDoc を起動し、キャプチャファイル (.rdc) を開く
2. MCP クライアント（Claude など）から RenderDoc のデータにアクセス

## 設計理念

本プロジェクトは、元の実装をベースに MCP ツールインターフェースの構成、命名の一貫性、呼び出し体験の最適化に重点を置いています。

より少なく、より安定した、より組み合わせやすいインターフェースで、より高頻度の RenderDoc 分析ニーズをカバーし、AI がチェーン呼び出しをしやすくすることを目指しています。

#### Canonicalization

類似機能は複数の意味的に近い MCP コマンドに分割するのではなく、統一されたエントリポイントに集約します。

例えば、複数の draw 検索インターフェースを `search_draws` に統合し、リソース列挙を `list_resources` に統一し、パラメータで型とクエリ次元を区別します。

#### Shape Consistency

異なるツールは、それぞれ独自の形式を定義するのではなく、一貫したパラメータスタイルと戻り値の構造に従うべきです。

例えば、ページネーション結果は `items / total_count / offset / limit` を統一して使用し、検索結果は `matches / total_matches / scanned_count` を統一して使用します。

#### Progressive Disclosure

MCP ツールセット全体は以下の 3 つの能力階層で構成されています：

- **グローバル操作能力**: capture / frame / resource space のナビゲーション、ターゲティング、グローバルサマリー — 「何を見るべきか、範囲はどれくらいか、どこから始めるか」に答える
- **局所データ分析能力**: 特定の event、shader、texture、buffer、mesh の深い分析 — 「この特定のポイントで何が起きたか」に答える
- **上位ツール能力**: エクスポート、保存、ダウンストリームワークフロー — 「どう再利用するか、リソースを見たい」に答える

![img.png](docs/images/organization.png)

## MCP ツール一覧

### グローバル操作能力

- `open_capture` - MCP クライアントから直接キャプチャファイルを開く
- `list_captures` - ディレクトリ内の `.rdc` ファイルを一覧表示
- `get_capture_status` - キャプチャの読み込み状態を確認
- `get_frame_summary` - フレーム全体の統計とトップレベルマーカーサマリーを取得
- `get_draw_calls` - draw call / action 階層をフィルタ付きで取得
- `search_draws` - shader、texture、resource で draw call を統一検索
- `list_resources` - texture と buffer を 1 つのページネーションインターフェースで一覧表示

### 局所データ分析能力

- `get_draw_call_details` - 特定の draw call の詳細情報を取得
- `get_action_timings` - action の GPU タイミングを取得
- `get_shader_info` - shader 逆アセンブル、定数バッファ、バインディングを取得
- `get_pipeline_state` - 完全なパイプライン状態と簡潔な入出力テクスチャサマリーを取得
- `get_texture_info` - テクスチャメタデータを取得
- `get_texture_data` - テクスチャピクセルデータを取得 (Base64)
- `get_buffer_contents` - バッファ内容を取得 (Base64)
- `get_mesh_summary` - メッシュトポロジ、数量、属性、境界を取得
- `get_mesh_data` - ページネーションでメッシュデータを取得

### 上位ツール能力

- `save_texture` - テクスチャを画像ファイルに保存 (PNG/JPG/BMP/TGA/EXR/DDS/HDR)
- `export_mesh_csv` - ダウンストリームワークフロー向けにメッシュ CSV をエクスポート

## 使用例

### 推奨フロー

典型的な分析フローは通常：

`get_capture_status` / `get_frame_summary` → `get_draw_calls` / `search_draws` → `get_pipeline_state` / `get_shader_info` / `get_mesh_data`

### draw call のグローバル検索

```
search_draws(by="shader", query="Toon", stage="pixel")
search_draws(by="texture", query="CharacterSkin")
search_draws(by="resource", query="ResourceId::12345")
```

### リソースの一覧表示

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

`get_pipeline_state` のレスポンスには簡潔な `input_textures` / `output_textures` サマリーが含まれます。

### canonical ページネーションでメッシュデータを取得

```
get_mesh_data(event_id=1234, offset=0, limit=100)
get_mesh_data(event_id=1234, offset=100, limit=100)
```

### テクスチャデータの取得

```
# 2D テクスチャの mip 0 を取得
get_texture_data(resource_id="ResourceId::123")

# 特定の mip レベルを取得
get_texture_data(resource_id="ResourceId::123", mip=2)

# キューブマップの特定の面を取得 (0=X+, 1=X-, 2=Y+, 3=Y-, 4=Z+, 5=Z-)
get_texture_data(resource_id="ResourceId::456", slice=3)

# 3D テクスチャの特定の深度スライスを取得
get_texture_data(resource_id="ResourceId::789", depth_slice=5)
```

### バッファデータの部分取得

```
# バッファ全体を取得
get_buffer_contents(resource_id="ResourceId::123")

# オフセット 256 から 512 バイトを取得
get_buffer_contents(resource_id="ResourceId::123", offset=256, length=512)
```

### テクスチャをファイルに保存

```
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.png")
save_texture(resource_id="ResourceId::123", output_path="D:/output/texture.jpg", format_type="JPG")
```

## TODO

現在のバージョンでは、ツールインターフェースの簡素化、インターフェースの canonical 化、クロス API 互換性の強化、および RenderDoc Python 3.6 環境での拡張機能の適応に重点を置いています。

今後はテスト結果に基づいて互換レイヤーツールのクリーンアップを継続し、より高レベルな分析機能を段階的に追加する予定です（現在の計画はモデル組立関連の上位ツールの構築です）。ホットリロードモジュールの追加。

## ライセンス

MIT
