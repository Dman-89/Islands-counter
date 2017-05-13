# -*- coding: utf-8 -*-
"""
Created on Sat May 13 20:13:12 2017

@author: fialdm01
"""

def cnt_islands(islands):
    isl_count = 0
    neib_g = set()
    neib_l = set()
    
    def chk(islands, i,j):
        try:
            if islands[i][j] == 0:
                return None
            else:
                neib_l.add((i,j))
        except IndexError:
            return None
        
        return chk(islands, i+1,j), chk(islands, i,j+1) #, chk(islands, i-1,j), chk(islands, i,j-1)
    
    cnt_zero = 1    
    for i in range(len(islands)):
        for j in range(len(islands[i])):
            if islands[i][j] == 1 and (i,j) not in neib_g:            
                                
                chk(islands, i,j)
                for x in neib_l:
                    if x in neib_g:
                        cnt_zero = 0
#                        print(x)
                        break
                neib_g.update(neib_l)
                neib_l = set()
                if cnt_zero == 1:
                    isl_count += 1
            cnt_zero = 1
    if isl_count == 0 and neib != set():
        isl_count = 1
    return isl_count

chk(tst1, 0,0)




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
tst6=[[0,0,1],
      [0,0,0],
      [0,1,0]]
#2
tst7=[[0,1,1],
      [0,0,0],
      [0,1,0]]
#2
tst8=[[0,0,1],
      [0,0,0],
      [0,1,0],
      [1,1,1]]
#2
tst9=[[1,0,1],
      [0,1,0],
      [0,0,1]]
#4
tst10=[[1,1,1,1],
       [0,1,0,0],
       [0,0,1,0]]
#2
tst11=[[1,1,1,1],
       [0,1,0,0],
       [0,0,1,0],
       [1,1,0,0]]
#3
tst12=[[1,1,1,1,0],
       [0,1,0,0,1],
       [0,0,1,0,1],
       [1,1,0,0,0]]
#4       
tst13=[[1,1,1,0,0,0,0],
       [0,0,1,0,1,0,1],
       [0,1,1,0,1,0,0],
       [1,1,1,1,1,0,0]]
#2
tst14=[[1,0,1,0,0,0,0],
       [0,0,1,0,0,0,1],
       [0,0,0,0,0,0,0],
       [1,1,1,1,1,0,0]]
#4
tst15=[[1,1,0,0,1,0,0],
       [1,0,1,0,1,0,1],
       [1,0,0,0,1,0,0],
       [1,1,1,1,1,0,0]]
#3
tst16=[[1,1,1],
       [0,0,1],
       [1,1,1]]
#1
tst17=[[1,1,0,0,1,0,0],
       [1,0,1,0,1,0,1],
       [1,0,0,0,1,0,0],
       [1,1,0,1,1,0,0]]
#4

assert cnt_islands(tst1) == 1
assert cnt_islands(tst2) == 1
assert cnt_islands(tst3) == 2
assert cnt_islands(tst4) == 2
assert cnt_islands(tst5) == 2
assert cnt_islands(tst6) == 2
assert cnt_islands(tst7) == 2
assert cnt_islands(tst8) == 2
assert cnt_islands(tst9) == 4
assert cnt_islands(tst10) == 2
assert cnt_islands(tst11) == 3
assert cnt_islands(tst12) == 4
assert cnt_islands(tst13) == 2
assert cnt_islands(tst14) == 4
assert cnt_islands(tst15) == 3
assert cnt_islands(tst16) == 1
assert cnt_islands(tst17) == 4
