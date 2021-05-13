#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2021/5/9 6:32 下午
# @Author   : Hanyiik
# @File     : TSP_GA_w.py
# @Function : 用 GA 解决 TSP 问题的可视化版

import random
import math
import sys
from GA import GA
import tkinter as Tkinter


class TSP_WIN(object):
    def __init__(self, aRoot, aLifeCount=100, aWidth=560, aHeight=330):
        self.isRunning = False
        self.nodes2 = []
        self.nodes = []
        self.cities = []
        self.root = aRoot
        self.lifeCount = aLifeCount
        self.width = aWidth
        self.height = aHeight
        self.canvas = Tkinter.Canvas(
            self.root,
            width=self.width,
            height=self.height,
        )
        self.canvas.pack(expand=Tkinter.YES, fill=Tkinter.BOTH)
        self.bindEvents()
        self.initCities()
        self.new()
        self.title("TSP")
        self.ga = GA(aCrossRate=0.7,
                     aMutationRage=0.02,
                     aLifeCount=self.lifeCount,
                     aGeneLength=len(self.cities),
                     aMatchFun=self.matchFun())

    def initCities(self):
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

        # 坐标变换
        minX, minY = self.cities[0][0], self.cities[0][1]
        maxX, maxY = minX, minY
        for city in self.cities[1:]:
            if minX > city[0]:
                minX = city[0]
            if minY > city[1]:
                minY = city[1]
            if maxX < city[0]:
                maxX = city[0]
            if maxY < city[1]:
                maxY = city[1]

        w = maxX - minX
        h = maxY - minY
        xoffset = 30
        yoffset = 30
        ww = self.width - 2 * xoffset
        hh = self.height - 2 * yoffset
        xx = ww / float(w)
        yy = hh / float(h)
        r = 5
        for city in self.cities:
            x = (city[0] - minX) * xx + xoffset
            y = hh - (city[1] - minY) * yy + yoffset
            self.nodes.append((x, y))
            node = self.canvas.create_oval(x - r, y - r, x + r, y + r,
                                           fill="#ff0000",
                                           outline="#000000",
                                           tags="node", )
            self.nodes2.append(node)

    def distance(self, order):
        distance = 0.0
        for i in range(-1, len(self.cities) - 1):
            index1, index2 = order[i], order[i + 1]
            city1, city2 = self.cities[index1], self.cities[index2]
            distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
        return distance

    def matchFun(self):
        return lambda life: 1.0 / self.distance(life.gene)

    def title(self, text):
        self.root.title(text)

    def line(self, order):
        self.canvas.delete("line")
        for i in range(-1, len(order) - 1):
            p1 = self.nodes[order[i]]
            p2 = self.nodes[order[i + 1]]
            self.canvas.create_line(p1, p2, fill="#000000", tags="line")

    def bindEvents(self):
        self.root.bind("n", self.new)
        self.root.bind("g", self.start)
        self.root.bind("s", self.stop)

    def new(self):
        order = range(len(self.cities))
        self.line(order)

    def start(self):
        self.isRunning = True
        while self.isRunning:
            self.ga.next()
            self.distance(self.ga.best.gene)
            self.line(self.ga.best.gene)
            self.title("TSP-gen: %d" % self.ga.generation)
            self.canvas.update()

    def stop(self):
        self.isRunning = False

    def mainloop(self):
        self.root.mainloop()


def main():
    tsp = TSP_WIN(Tkinter.Tk())
    tsp.mainloop()


if __name__ == '__main__':
    main()