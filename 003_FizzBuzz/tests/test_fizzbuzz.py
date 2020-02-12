#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from src.fizzbuzz import FizzBuzz

@pytest.mark.parametrize('data, expected',[
    (0,"FizzBuzz!"),
    (1,1),
    (2,2),
    (3,"Fizz!"),
    (3.0,"Fizz!"),
    (4,4),
    (5,"Buzz!"),
    (6,"Fizz!"),
    (7,7),
    (8,8),
    (9,"Fizz!"),
    (10,"Buzz!"),
    (11,11),
    (12,"Fizz!"),
    (13,13),
    (14,14),
    (15,"FizzBuzz!"),
    (16,16),
    (17,17),
    (18,"Fizz!"),
    (19,19),
    (20,"Buzz!")
])
def test(data,expected):
    fz = FizzBuzz(data)
    assert fz.fizzbuzz == expected

def test_文字入力():
    try:
        fz = FizzBuzz("a")
        assert False
    except TypeError:
        assert True

def test_スペース入力():
    try:
        fz = FizzBuzz(" ")
        assert False
    except TypeError:
        assert True

def test_全角数値入力():
    try:
        fz = FizzBuzz("１")
        assert False
    except TypeError:
        assert True

