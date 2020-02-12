#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
from src.greet import Greet

def test():
    gr = Greet()
    assert gr.greet() == 'hello world'

