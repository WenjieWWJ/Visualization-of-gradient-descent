#coding:utf-8
import json
import numpy as np
from tf_gd import GradientDescentTest1
a_list,b_list,cost_list,x_list,y_list,results_list=GradientDescentTest1()

test={}
print np.array(a_list,dtype = np.float32)
test['a'] = np.array(a_list).tolist()
test['b'] = [5.0,1.0,4.99999]
print test
j = json.dumps(test)
print j
