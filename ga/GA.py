#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2021/5/9 6:03 下午
# @Author   : Hanyiik
# @File     : GA.py
# @Function : 遗传算法类 GA

import random
from Life import Life


class GA(object):

    def __init__(self, aCrossRate, aMutationRage, aLifeCount, aGeneLength, aMatchFun = lambda life : 1):
        self.crossRate = aCrossRate             # 交叉率
        self.mutationRate = aMutationRage       # 变异率
        self.lifeCount = aLifeCount             # 种群中的个体数量
        self.geneLength = aGeneLength           # 基因长度
        self.matchFun = aMatchFun               # 适配函数
        self.lives = []                         # 种群
        self.best = None                        # 保存这一代中最好的个体

        self.generation = 1                     # 第几代
        self.crossCount = 0                     # 统计: 交叉了几次？
        self.mutationCount = 0                  # 统计: 变异了几次？
        self.bounds = 0.0                       # 适配值之和，用于选择是计算概率

        self.initPopulation()


    def initPopulation(self):
        """
        :: 功能: 种群初始化
        :: 输入: self -
        :: 输出:
        :: 用法:
        """
        self.lives = []
        for i in range(self.lifeCount):
            gene = [x for x in range(self.geneLength)]
            random.shuffle(gene)
            life = Life(gene)
            self.lives.append(life)


    def judge(self):
        """
        :: 功能: 评估，计算每一个个体的适配值
        :: 输入: self -
        :: 输出:
        :: 用法:
        """
        self.bounds = 0.0
        self.best = self.lives[0]
        for life in self.lives:
            life.score = self.matchFun(life)
            self.bounds += life.score
            if self.best.score < life.score:
                self.best = life


    def cross(self, parent1, parent2):
        """
        :: 功能: 交叉
        :: 输入: self, parent1, parent2 -
        :: 输出:
        :: 用法:
        """
        index1 = random.randint(0, self.geneLength - 1)
        index2 = random.randint(index1, self.geneLength - 1)
        tempGene = parent2.gene[index1:index2]  # 交叉的基因片段
        newGene = []
        p1len = 0
        for g in parent1.gene:
            if p1len == index1:
                newGene.extend(tempGene)  # 插入基因片段
                p1len += 1
            if g not in tempGene:
                newGene.append(g)
                p1len += 1
        self.crossCount += 1
        return newGene


    def mutation(self, gene):
        """
        :: 功能: 变异
        :: 输入: self, gene -
        :: 输出:
        :: 用法:
        """
        index1 = random.randint(0, self.geneLength - 1)
        index2 = random.randint(0, self.geneLength - 1)

        newGene = gene[:]  # 产生一个新的基因序列，以免变异的时候影响父种群
        newGene[index1], newGene[index2] = newGene[index2], newGene[index1]
        self.mutationCount += 1
        return newGene


    def getOne(self):
        """
        :: 功能: 选择一个个体
        :: 输入: self -
        :: 输出:
        :: 用法:
        """
        r = random.uniform(0, self.bounds)
        for life in self.lives:
            r -= life.score
            if r <= 0:
                return life

        raise Exception("选择错误", self.bounds)


    def newChild(self):
        """
        :: 功能: 产生新后代
        :: 输入: self -
        :: 输出:
        :: 用法:
        """
        parent1 = self.getOne()
        rate = random.random()

        # 按概率交叉
        if rate < self.crossRate:
            # 交叉
            parent2 = self.getOne()
            gene = self.cross(parent1, parent2)
        else:
            gene = parent1.gene

        # 按概率突变
        rate = random.random()
        if rate < self.mutationRate:
            gene = self.mutation(gene)

        return Life(gene)


    def next(self):
        """
        :: 功能: 产生下一代
        :: 输入: self -
        :: 输出:
        :: 用法:
        """
        self.judge()
        newLives = [self.best]
        while len(newLives) < self.lifeCount:
            newLives.append(self.newChild())
        self.lives = newLives
        self.generation += 1