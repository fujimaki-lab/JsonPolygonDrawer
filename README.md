# JsonPolygonDrawer

複雑な折り紙のポリゴンデータを可視化する Python スクリプトです。  
JSON ファイルからポリゴン座標を読み込み、個別の画像や全ポリゴンをまとめた画像を生成できます。

## 機能

- JSON ファイル (`polygons.json` 形式) からポリゴンデータを読み込み
- 各ポリゴンを個別画像として保存
- 全ポリゴンをまとめて 1 枚の画像として保存
- 描画座標を固定（X, Z 座標: -5.5 ～ 5.5）
- 中心に ID を表示して確認可能

## 必要環境

- Python 3.7 以上
- matplotlib

インストール例:

```bash
pip install matplotlib
