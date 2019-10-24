from networkx import *
from networkx.algorithms import approximation as approx
import random
import numpy as np
import copy
import time



G = erdos_renyi_graph(100, 0.05, seed=123, directed=True)
for (i,j) in list(nx.edges(G)):
    G[i][j]['relia']=np.random.uniform(0.6, 0.95)

def regraph(G):
    ng=number_of_edges(G)
    rs=np.random.uniform(0,1,ng)
    k,ebunch=0,[]
    for (i,j) in list(nx.edges(G)):
        if G[i][j]['relia']<rs[k]:
            ebunch.append((i,j))
        k+=1
    gg=copy.deepcopy(G)
    gg.remove_edges_from(ebunch)
    return gg


def relia2(G,x,s,t,i=0):
    r=dict()
    for (si,ti) in zip(s,t):
        r['r_%s_%s'%(si,ti)]=0
      
    for _ in range(x):
        gg=regraph(G)
        for (si,ti) in zip(s,t):
            if has_path(gg,si,ti):
               r['r_%s_%s'%(si,ti)]+=1
    
    for (si,ti) in zip(s,t):
      print('r_%s_%s'%(si,ti),"=",r['r_%s_%s'%(si,ti)]/x)

import time
s,t=[1,3,5,7],[19,17,16,15]
for i in range(3):
    tStart = time.time()
    relia2(G,10000,s,t)
    tEnd=time.time()
    print('\n',tEnd - tStart)
    print("--------------------------")

