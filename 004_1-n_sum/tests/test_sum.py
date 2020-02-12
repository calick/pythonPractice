#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from src.calc import sum

@pytest.mark.parametrize('data, expected',[
    (0,0),
    (1,1),
    (2,3),
    (3,6),
    (4,10),
    (5,15),
    (6,21),
    (7,28),
    (8,36),
    (9,45),
    (10,55),
    (100,5050),
    (1000,500500),
])
def test(data,expected):
    assert sum(data) == expected