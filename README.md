# Getting Started
* HeadlessCMSのstrapiとそれを利用するフロントエンド環境の連携サンプルです
* Node v12~, Python 3.7~
## 準備
* ```$ pip install -r requirements.txt ``` して、必要なPythonライブラリをインストールします
* strapi-server ディレクトリに移動し``` $ yarn install ``` してください
* strapiにCOLLECTION TYPES, SINGLE TYPESそれぞれ定義しています
  * COLLECTION TYPES
    * post
  * SINGLE TYPES
    * test-single
* APIのエンドポイントとしてhttp://localhost:1337/posts を利用します
## 動かす
* strapi-serverディレクトリに移動し、yarn developを実行してください。strapiサーバが起動します
* ディレクトリルートにあるserver.pyを起動してください. Flaskサーバが起動します
* http://127.0.0.1:5000/posts にアクセスすることで、strapiサーバのAPIからコンテンツを取得していることを確認できます
