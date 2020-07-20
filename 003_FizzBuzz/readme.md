
# 概要

まずは一般的な問題。

FizzBuzz

入力に対して以下を出力

3の倍数の時は「Fizz!」を出力
5の倍数の時は「Buzz!」を出力
15の倍数の時は「FizzBuzz!」を出力
それ以外の時は入力された数値をそのまま出力する。
入力された値が数値以外であれば「!!Error!!」を出力

# 環境構築

pip install -e .

* テストが終わったら削除  
pip uninstall fizzbuzz

# 環境構築（pipenvを使う場合）

pipenv --python 3
pipenv install -e .
pipenv shell

* テストが終わったら削除  
pipenv --rm

# ツールの実行

fizzbuzz -d [int:数値]

# テストの実行

pytest

