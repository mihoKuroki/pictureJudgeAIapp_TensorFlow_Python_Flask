#画像データをNumPy配列に変換する
from PIL import Image
import os,glob
import numpy as np
from sklearn import model_selection
from pprint import pprint

classes = ["櫻井翔", "大野智","二宮和也"]
num_classes = len(classes)
image_size = 50


#画像の読み込み
X = []  #画像データ
Y = []  #ラベルデータ
for index, classlabel in enumerate(classes):
    photos_dir = "./" + classlabel  #画像が保存されているディレクトリ
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 30: break
        image = Image.open(file)  #画像を開く
        image = image.convert("RGB")  #色空間をRGBに
        image = image.resize((image_size, image_size))  #画像サイズを50*50に変換
        data = np.asarray(image)  #NumPy配列に変換
        X.append(data)  #asarrayでNumPy配列に変換
        Y.append(index)  #ラベルを追加
        
X = np.array(X)  #NumPy配列に変換
Y = np.array(Y)
# pprint(Y)
#学習データとテストデータを分ける
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
# xy = (X_train, X_test, y_train, y_test)
# pprint(len(xy[0]))  #40
# pprint(len(xy[1]))  #14
# pprint(len(xy[2]))  #40
# pprint(len(xy[3]))  #14
# pprint(X_train.shape)
# pprint(X_test.shape)
# pprint(y_train.shape)
# pprint(y_test.shape)

np.save("./animal_X_train.npy", X_train)  #NumPy配列をバイナリファイルに保存
np.save("./animal_X_test.npy", X_test)
np.save("./animal_y_train.npy", y_train)
np.save("./animal_y_test.npy", y_test)
# X_train = np.save("./X_train.npy",allow_pickle=True)
# X_test = np.save("./X_test.npy",allow_pickle=True)
# y_train = np.save("./y_train.npy",allow_pickle=True)
# y_test = np.save("./y_test.npy",allow_pickle=True)