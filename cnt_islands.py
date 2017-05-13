# -*- coding: utf-8 -*-
"""
Created on Sat May 13 20:13:12 2017

@author: fialdm01
"""

def cnt_islands(islands):
    isl_count = 0
    neib_cnt = set()
    for i in range(len(islands)):
        for j in range(len(islands[i])):
            if islands[i][j] == 1:                
                try:
                    if islands[i+1][j] == 1:
                        neib_cnt.add((i+1, j))
                        neib_cnt.add((i, j))
                    if islands[i][j+1] == 1:
                        neib_cnt.add((i, j+1))
                        neib_cnt.add((i, j))
                except IndexError:
                     pass
                                    
    if isl_count == 0 and neib_cnt != set():
        isl_count = 1
    return isl_count

cnt_islands(tst1)
cnt_islands(tst2)
cnt_islands(tst3)
cnt_islands(tst4)
cnt_islands(tst5)







tst1=[[1,0,1],
      [1,0,1],
      [1,1,1]]
#1
tst2=[[0,1,1],
      [0,1,1],
      [0,0,0]]
#1
tst3=[[0,0,1],
      [0,1,0],
      [0,0,0]]
#2
tst4=[[0,0,1],
      [0,0,0],
      [0,1,0]]
#2
tst5=[[1,0,1],
      [1,1,0],
      [0,0,0]]
#2
