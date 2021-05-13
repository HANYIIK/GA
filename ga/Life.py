#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2021/5/9 6:30 下午
# @Author   : Hanyiik
# @File     : Life.py
# @Function : 种群中的个体类 Life

SCORE_NONE = -1

class Life(object):
      def __init__(self, aGene = None):
            self.gene = aGene
            self.score = SCORE_NONE