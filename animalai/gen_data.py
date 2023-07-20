#画像データをNumPy配列に変換する
from PIL import Image
import os,glob
import numpy as np
from sklearn import model_selection
from pprint import pprint

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50


#画像の読み込み
X = []  #画像データ
Y = []  #ラベルデータ
for index, classlabel in enumerate(classes):
    photos_dir = "./" + classlabel
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 30: break
        image = Image.open(file)  #画像を開く
        image = image.convert("RGB")  #色空間をRGBに
        image = image.resize((image_size, image_size))  #画像サイズを50*50に変換
        data = np.asarray(image)  #NumPy配列に変換
        X.append(data)  #asarrayでNumPy配列に変換
        Y.append(index)  #ラベルを追加
        
X = np.array(X, dtype=np.float32)  #NumPy配列に変換
Y = np.array(Y, dtype=np.int32)
# pprint(Y)
#学習データとテストデータを分ける
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
# pprint(xy)
np.save("./animal.npy", xy)  #NumPy配列をバイナリファイルに保存
