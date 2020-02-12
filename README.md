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

環境情報

```py:
> python -V
Python 3.7.1
```

* pytestの環境を準備する  
pip install pytest  
pip install pytest-cov  

→ setup.pyが置いてあれば基本的に　「pip install -e .」を実行すればOK  




