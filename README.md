# pythonで実装の練習

## 簡単な機能を作ってみる

pytestでテストファーストで書いていく。

1. hello world (クラス)
1. hello world (コマンドラインツール,クラス)
1. FizzBuzz:fizzbuzz問題 (コマンドラインツール,クラス,pytest_mark_同じメソッドのテストを引数を変えてテストする,argparse_パラメータ引数)
1. 1-n_sum:1からnまでの和 (関数呼び出し,for,pytest_mark_同じメソッドのテストを引数を変えてテストする,argparse_パラメータ引数)
1. PrintPrimeNumber:素数を表示 (関数呼び出し,for,pytest_mark_同じメソッドのテストを引数を変えてテストする,argparse_パラメータ引数)






#### 参考

「自作Python100本ノック」１日目（はじめに〜5本目）
https://qiita.com/ahpjop/items/373f807d68044cda1c9b

pytestに入門してみたメモ
https://qiita.com/everylittle/items/1a2748e443d8282c94b2



# 環境構築

環境情報（ドキュメント作成時の情報）

```py:
> py -V
Python 3.8.1
```

* pytestの環境を準備する  
pip install pytest  
pip install pytest-cov  

* pipenvの環境を準備する
pip install pipenv

* pipenvの操作関連
```
■python3系の環境
pipenv --python 3
■使用するパッケージのinstall
pipenv install xxxx 
■開発環境のみで使うパッケージを別枠で管理しながらインストールも可能
pipenv install --dev xxxx yyyy
■requirements.txtからのinstall
pipenv install -r ./requirements.txt
■Pipfileからの環境再現
pipenv install 
pipenv install --dev
■PipfileでなくPipfile.lockから詳細なバージョンなども併せて環境を作成したい場合
pipenv sync
pipenv sync --dev
■スクリプトの登録は以下を参照
https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a#christmas_tree%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88%E3%81%AE%E7%99%BB%E9%8C%B2
■pipenvで作られた仮想環境へ入る
pipenv shell
■仮想環境のパスを調べる
pipenv --venv
■仮想環境を削除する
pipenv --rm
```

* 

* ｘｘｘ
→ setup.pyが置いてあれば基本的に　「pip install -e .」を実行すればOK  




