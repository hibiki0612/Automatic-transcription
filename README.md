# 制作物名:「Automatic transcription」

##機能
new memoでメモを作成
このとき，stt startを押すと，文字認識が行われる.
*GoogleChoneのみ対応
memolistにメモが保存され，そのmemolistに保存されたメモは，Transrate Memoで要約が行われる

現在，個別で使えるようにアカウント作成を行なっている．
また，文字起こし，要約はAPIを使っているため，今後自分で作ったモデルを実装予定

##使い方
## 使い方
1. このリポジトリをクローン
2. mecabをインストール
3. pysummarizationをインストール
4. 以下を実行

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
3. ブラウザで http://127.0.0.1:8000/ を開く
