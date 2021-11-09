#!/usr/bin/python -S
# coding: utf-8

import time
print("カウントダウンをします。5秒前")

count = 5

while(1):
    print(count)
    count -= 1
    time.sleep(1)

    if count == 0:
        print("ゼロ！")
        break

