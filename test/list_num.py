#!/usr/bin/python -S
# coding: utf-8

colorlist = [["red", "赤"], ["blue", "青"],["green", "緑", "みどり"], ["white", "白"], ["black", "黒"], ["pink", "ピンク"], ["yellow"]]

print("row:", len(colorlist))

for n in range(len(colorlist)):
    print("column", len(colorlist[n]))