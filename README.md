# 人物写真から棒人間を生成するツール

このプロジェクトは、Python と MediaPipe を使用して写真内の人物の姿勢を検出し、その結果をもとに簡易的な棒人間（スティックフィギュア）として描画するものです。

## 特徴

* MediaPipe の姿勢推定を用いて人物のランドマーク（関節）を検出
* 検出されたキーポイントに基づいて棒人間を描画
* 出力画像に棒人間を重ねて保存（オプションで重ねないことも可能）

## 必要な環境

* Python 3.7 以上
* mediapipe
* opencv-python
* numpy

必要なパッケージは以下でインストールできます：

```bash
pip install -r requirements.txt
```

## ディレクトリ構成

```
.
├── inputs/
│   └── input.jpg
├── outputs/
│   └── output.jpg
├── scripts/
│   └── stick_figure.py
├── .gitignore
├── LICENSE
├── README.md(今ここ)
└── requirements.txt
```

## 使い方

プロジェクトのルートディレクトリから以下のコマンドを実行します：

```bash
python scripts/stick_figure.py --input inputs/input.jpg --output outputs/output.jpg --overlay True
```

`--overlay` オプションを `True` に設定すると元画像に棒人間を重ねて保存し、`False` にすると白背景に棒人間のみを描画します。

## 注意事項

* 入力画像には人物が明確に写っている必要があります。正しく姿勢を検出するために、顔や体全体が見える画像を推奨します。
* 出力画像は `outputs/output.jpg` に保存されます。

## ライセンス

MIT [License](./LICENSE)

---

MediaPipe と OpenCV に感謝して ❤️
