# -*- coding: utf-8 -*-
"""
int array: boxes and lemons，一个代表箱子的大小，一个代表西瓜的大小，每个箱子最多只能装一个小于等于它size的西瓜。
在西瓜size array选择起点i,放到任意可放的箱子位置，i之后连续的西瓜i+1,i+2…
都要找到箱子放进去且箱子中西瓜的相对顺序需要保持原来的顺序。求最多可放在箱子里的西瓜序列的长度（西瓜数）

@author: User
"""

boxes = (1, 3, 4, 5, 6, 8, 10)
lemons = (3,2,1)

boxes_list = list(boxes)

start = 0
n = 0
box1 = boxes_list[:]
print box1
for i in range(start, len(lemons)):
    while len(box1) > 0:
        box = box1.pop(0)
        print lemons[-i-1]
        if box >= lemons[-i-1]:
            n += 1
            break

m = 0
box2 = boxes_list[:]
print box2
for i in range(start, len(lemons)):
    while len(box2) > 0:
        box = box2.pop(0)
        print lemons[i]
        if box >= lemons[i]:
            m += 1
            break        
        
print(max(n,m))