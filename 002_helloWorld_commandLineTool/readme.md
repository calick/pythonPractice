# 概要

最初は「Hello World」

呼び出しをしたらコンソール上に「Hello World」が出力される。

# 環境構築

pip install -e .

* テストが終わったら削除  
pip uninstall helloWorld

# 環境構築（pipenvを使う場合）

pipenv --python 3
pipenv install -e .
pipenv shell

* テストが終わったら削除  
pipenv --rm

# ツールの実行

helloWorld

# テストの実行

pytest

