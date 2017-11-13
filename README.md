# PythonでOpenCVを触ってみる
## ファイル概要
### 画像を読み込んで表示する 
`Processing2.x`で実行できます  
[OutputImage.pyde](https://github.com/y-zumi/processing-python/tree/master/OutputImage)

### 画像の色情報（HSV値）を取得する（特徴量1）
`Processing2.x`で実行できますが，`opencv`を追加する必要があります  
[Color.pyde](https://github.com/y-zumi/processing-python/tree/master/color)

### 画像の輪郭と面積から円形度を算出する（特徴量2）
`Python3.x`と`OpenCV3`で実装しているため`Processing2.x`では動きません  
[circularity.py](https://github.com/y-zumi/processing-python/blob/master/opencv-python/circularity.py)

### 特徴量1と特徴量2に基づきクラスタリングを行う
`Processing2.x`で実行できます
[clustering.pyde](https://github.com/y-zumi/processing-python/tree/master/clustering)
