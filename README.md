# p3d-ray.py

## 日本語

`p3d-ray.py` は、Processing ライクな書き方で 3D 空間を記述し、レイトレーシングで描画するための Python ライブラリです。CG 基礎の最終課題として作成されたフルスクラッチ実装で、ビジュアルプログラミングの結果をレイトレーシングすることを目的にしています。

参考: https://www.honma.site/ja/works/P3DRay/

### 特徴

- `translate`、`rotateY`、`box` などの Processing 風 API
- 環境テクスチャの設定
- マテリアル設定
- サンプル数を指定した render
- Python だけで試せる小さなレイトレーシング実験環境

### 必要環境

- Python 3
- NumPy
- OpenCV (`cv2`)

```bash
pip install numpy opencv-python
```

### サンプルコード

`main.py` には次のような最小サンプルが入っています。

```python
from p3dray import *

set_environment_texture("meadow_2_2k.jpg")

rotateY(radians(30))
translate(0, 0, 5)

set_material(base_color=[1, 0.8, 0.8], metalic=1, roughness=1)
box(2.2, 2.2, 2.2)

render(sample_N=5)
```

### 実行

```bash
python main.py
```

### 構成

- `p3dray/`: ライブラリ本体
- `p3dray/renderer`: レンダリング処理
- `p3dray/primitive`: `box` などのプリミティブ
- `p3dray/material`: マテリアルとテクスチャ
- `p3dray/coordinate`: 座標変換
- `main.py`: サンプル
- `play.py`: 実験用スクリプト
- `*.jpg`, `*.png`, `*.exr`: サンプルアセット

## English

`p3d-ray.py` is a Python ray-tracing experiment that lets users describe 3D scenes with Processing-like APIs.

Reference: https://www.honma.site/ja/works/P3DRay/

### Features

- Processing-like APIs such as `translate`, `rotateY`, and `box`
- Environment texture support
- Material setup
- Sample-count based rendering
- Small scratch-built ray-tracing environment in Python

### Requirements

- Python 3
- NumPy
- OpenCV (`cv2`)

```bash
pip install numpy opencv-python
```

### Example

```python
from p3dray import *

set_environment_texture("meadow_2_2k.jpg")

rotateY(radians(30))
translate(0, 0, 5)

set_material(base_color=[1, 0.8, 0.8], metalic=1, roughness=1)
box(2.2, 2.2, 2.2)

render(sample_N=5)
```

### Run

```bash
python main.py
```
