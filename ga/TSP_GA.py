#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2021/5/9 6:31 下午
# @Author   : Hanyiik
# @File     : TSP_GA.py
# @Function : 用 GA 解决 TSP 问题
import pdb
import random
import math
import csv
from GA import GA


class City(object):
    def __init__(self, aName, aPos):
        self.name = aName
        self.pos = aPos


class TSP(object):
    def __init__(self, aCrossRate, aMutationRage, aLifeCount):
        self.cities = []
        self.initCities()
        self.ga = GA(aCrossRate=aCrossRate,                                     # 交叉率
                     aMutationRage=aMutationRage,                               # 变异率
                     aLifeCount=aLifeCount,                                     # 一个种群中的个体数
                     aGeneLength=len(self.cities),                              # 基因长度 = 城市数量 = 34
                     aMatchFun=lambda life: 1.0 / self.distance(life.gene))     # 距离越长，适应度越低

    def initCities(self):
        """
        :: 功能: 初始化中国 34 个城市的 [名称] + [经纬度]
        :: 输入: NULL
        :: 输出: 由 34 个 City 类组成的 self.cities(由 .csv 文件所确定)
        :: 用法: self.cities = []
                self.initCities()
        """
        with open('../data/china.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                name, longitude, latitude = row[0].split(';')
                pos = (float(longitude), float(latitude))
                self.cities.append(City(name, pos))

    def distance(self, order):
        """
        :: 功能: 计算城市排序的总距离
        :: 输入: order - 一个个体的基因，即城市排列顺序
        :: 输出: 总距离
        :: 用法: distance = self.distance(life.gene)
        """
        distance = 0.0
        for i in range(-1, len(self.cities) - 1):
            index1, index2 = order[i], order[i + 1]
            city1, city2 = self.cities[index1].pos, self.cities[index2].pos

            # distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

            R = 6371.004
            Pi = math.pi
            LatA = city1[1]
            LatB = city2[1]
            MLonA = city1[0]
            MLonB = city2[0]

            C = math.sin(LatA*Pi / 180) * math.sin(LatB * Pi / 180) + math.cos(LatA * Pi / 180) * math.cos(LatB * Pi / 180) * math.cos((MLonA - MLonB) * Pi / 180)
            D = R * math.acos(C) * Pi / 100
            distance += D

        return distance

    def run(self, Gen=0):
        while Gen > 1:
            self.ga.next()      # 产生下一代
            distance = self.distance(self.ga.best.gene)
            print("%d : %f" % (self.ga.generation, distance))   # 把这一代最好的个体的总距离 print 出来
            Gen -= 1


if __name__ == '__main__':
    tsp = TSP(aCrossRate=0.9, aMutationRage=0.3, aLifeCount=200)
    tsp.run(Gen=10000)