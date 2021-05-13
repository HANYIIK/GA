#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2021/5/9 6:31 下午
# @Author   : Hanyiik
# @File     : TSP_GA.py
# @Function : 用 GA 解决 TSP 问题

import random
import math
from GA import GA


class TSP(object):
    def __init__(self, aLifeCount=100):
        self.cities = []
        self.initCities()
        self.lifeCount = aLifeCount
        self.ga = GA(aCrossRate=0.7,
                     aMutationRage=0.3,
                     aLifeCount=self.lifeCount,
                     aGeneLength=len(self.cities),
                     aMatchFun=self.matchFun())

    def initCities(self):
        """
        for i in range(34):
              x = random.randint(0, 1000)
              y = random.randint(0, 1000)
              self.cities.append((x, y))
        """
        # 中国34城市经纬度
        self.cities.append((116.46, 39.92))
        self.cities.append((117.2, 39.13))
        self.cities.append((121.48, 31.22))
        self.cities.append((106.54, 29.59))
        self.cities.append((91.11, 29.97))
        self.cities.append((87.68, 43.77))
        self.cities.append((106.27, 38.47))
        self.cities.append((111.65, 40.82))
        self.cities.append((108.33, 22.84))
        self.cities.append((126.63, 45.75))
        self.cities.append((125.35, 43.88))
        self.cities.append((123.38, 41.8))
        self.cities.append((114.48, 38.03))
        self.cities.append((112.53, 37.87))
        self.cities.append((101.74, 36.56))
        self.cities.append((117, 36.65))
        self.cities.append((113.6, 34.76))
        self.cities.append((118.78, 32.04))
        self.cities.append((117.27, 31.86))
        self.cities.append((120.19, 30.26))
        self.cities.append((119.3, 26.08))
        self.cities.append((115.89, 28.68))
        self.cities.append((113, 28.21))
        self.cities.append((114.31, 30.52))
        self.cities.append((113.23, 23.16))
        self.cities.append((121.5, 25.05))
        self.cities.append((110.35, 20.02))
        self.cities.append((103.73, 36.03))
        self.cities.append((108.95, 34.27))
        self.cities.append((104.06, 30.67))
        self.cities.append((106.71, 26.57))
        self.cities.append((102.73, 25.04))
        self.cities.append((114.1, 22.2))
        self.cities.append((113.33, 22.13))

    def distance(self, order):
        distance = 0.0
        for i in range(-1, len(self.cities) - 1):
            index1, index2 = order[i], order[i + 1]
            city1, city2 = self.cities[index1], self.cities[index2]
            distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

            """
            R = 6371.004
            Pi = math.pi 
            LatA = city1[1]
            LatB = city2[1]
            MLonA = city1[0]
            MLonB = city2[0]

            C = math.sin(LatA*Pi / 180) * math.sin(LatB * Pi / 180) + math.cos(LatA * Pi / 180) * math.cos(LatB * Pi / 180) * math.cos((MLonA - MLonB) * Pi / 180)
            D = R * math.acos(C) * Pi / 100
            distance += D
            """
        return distance

    def matchFun(self):
        return lambda life: 1.0 / self.distance(life.gene)

    def run(self, n=0):
        while n > 0:
            self.ga.next()
            distance = self.distance(self.ga.best.gene)
            print("%d : %f" % (self.ga.generation, distance))
            n -= 1


def main():
    tsp = TSP()
    tsp.run(10000)


if __name__ == '__main__':
    main()