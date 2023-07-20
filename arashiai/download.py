# Purpose: Download images from Flickr
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# API key　information
key = "42730be8bfbd2576233e2eea7fa0806c"
secret = "bfa8822bca1bfcb5"
wait_time = 1

#保存フォルダの指定
animalname = sys.argv[1]  ##コマンドラインから検索したいキーワードを入力
savedir = "./" + animalname  ##保存フォルダを指定

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animalname,
    per_page = 50,   ##取得するデータ件数
    media = 'photos',  ##写真を検索
    sort = 'relevance',  ##関連順にソート
    safe_search = 1,  ##安全なコンテンツのみ
    extras = 'url_q, licence'  ##取得する情報の指定
)

photos = result['photos']  ##検索結果の写真情報
# pprint(photos)  ##検索結果の写真情報を表示

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue  ##ファイルが存在する場合はスキップ
    urlretrieve(url_q, filepath)  ##url_qの画像をfilepathに保存
    time.sleep(wait_time)