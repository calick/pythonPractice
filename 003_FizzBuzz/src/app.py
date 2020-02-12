#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.fizzbuzz import FizzBuzz

# コマンドライン引数を受け取るためのimport
import argparse

# 数値を受け取るときのオプション
parser = argparse.ArgumentParser()
parser.add_argument('-d','--data',type=int,help='DATA : int',default=0)

# コマンドラインオプションのパース
args = parser.parse_args()

def main():
    fb = FizzBuzz(args.data)
    fb.printFizzBuzz()s