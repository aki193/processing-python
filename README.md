# PythonでOpenCVを触ってみる
## 画像を読み込んで表示する 
`Processing2.x`で実行できます  
[OutputImage.pyde](https://github.com/y-zumi/processing-python/tree/master/OutputImage)
### 画像出力の実行結果
<img width="724" alt="2017-11-13 22 21 01" src="https://user-images.githubusercontent.com/20827588/32727727-f74f7710-c8c0-11e7-8327-0e4dcfd03f02.png">

## 画像の色情報（HSV値）を取得する（特徴量1）
`Processing2.x`で実行できますが，`opencv`を追加する必要があります  
[Color.pyde](https://github.com/y-zumi/processing-python/tree/master/Color)

## 画像の輪郭と面積から円形度を算出する（特徴量2）
`Python3.x`と`OpenCV3`で実装しているため`Processing2.x`では動きません  
[Circularity.py](https://github.com/y-zumi/processing-python/tree/master/Circularity)
### 円形度実行結果
<img width="404" alt="2017-11-13 22 22 41" src="https://user-images.githubusercontent.com/20827588/32727787-338330a0-c8c1-11e7-90c8-6a1fe2ca48de.png">

## 特徴量1と特徴量2に基づきクラスタリングを行う
`Processing2.x`で実行できます 
[Clustering.pyde](https://github.com/y-zumi/processing-python/tree/master/Clustering)
### クラスタリング実行結果
|初期状態|最終状態|
|:--:|:--:|
|<img width="884" alt="2017-11-13 22 17 27" src="https://user-images.githubusercontent.com/20827588/32727638-8956c7f4-c8c0-11e7-9e0b-49b3ab89a2e0.png">|<img width="912" alt="2017-11-13 22 17 44" src="https://user-images.githubusercontent.com/20827588/32727644-8e7b3828-c8c0-11e7-8c60-33cf4634f144.png">|

## パーセプトロンを行う
- 青いプロットがタワシの特徴量を基につけたもの
- 緑プロットがウニの特徴量を基につけたもの  
### パーセプトロン実行結果
![output](https://user-images.githubusercontent.com/20827588/34651154-c57ae696-f40f-11e7-9874-c9e1ad59c0ca.gif)
