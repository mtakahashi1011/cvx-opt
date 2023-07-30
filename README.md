# cvx-opt
## Dockerfileからコンテナを起動する方法

### 1.リポジトリのクローン
以下のコマンドでリモートのリポジトリをクローンする
```bash
git clone https://github.com/mtakahashi1011/optimization.git
```
ユーザー名とアクセストークンを入力する

### 2.DockerfileからDockerイメージの作成
以下のコマンドでDockerfileからDockerイメージを作成する
```bash
docker image build -t (イメージ名) （Dockerfileのあるディレクトリのパス）
```
Dockerイメージの作成時に以下のコマンドが実行されることに注意する

pycddlibをbuildするためのgccのインストール
```bash
apt update
apt install -y gcc
```

必要なライブラリのインストール
```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools
python3 -m pip install -r requirements.txt
```
`Could not open '/lib64/ld-linux-x86-64.so.2': No such file or directory`というエラーに対処するために`FROM`行に`--platform=linux/amd64`を加えている

以下のURLを参考にした

https://qiita.com/silloi/items/739699337b9bf4883b3e

また，その他のパッケージはcvxotのインストールのために必要なものであり以下のURLを参考にした

https://cvxopt.org/install/#ubuntu-debian

https://github.com/cvxopt/cvxopt/issues/78


### 3.コンテナの起動
以下のコマンドでDockerコンテナの起動
```bash
docker container run -it -p 8957:8888 --name (コンテナ名) （イメージ名）
```
ポートフォワーディングのためのホスト側のポート番号（左側のポート番号）は任意に設定して良い

### ４.テストコードの実行
以下のコマンドでテストコードを実行する
```bash
python3 linear_opt/linear_opt.py
```

### ５.JupyterLabの起動
JupyterLabで作業をしたい場合には以下のコードで起動する
```bash
jupyter-lab --ip=0.0.0.0 --port=8888 --allow-root --no-browser
```
http://localhost:8957 でJupyterLabにアクセスする

その際に認証トークンが必要なので注意する
