#coding:utf-8
from __future__ import unicode_literals

import tensorflow as tf
import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

def GradientDescentTest1(function=1,lr=0.01,real_params=[1.2, 2.5,0],init_params=[5, 1],iter_num=400,point_num=30):
	LR = lr
	REAL_A = real_params[0]
	REAL_B = real_params[1]
	REAL_C = real_params[2]
	print "real:",real_params
	INIT_PARAMS = init_params
					# [[5, 4],
	    #            [5, 1],
	    #            [2, 4.5]][1]
	print "init: ",init_params
	x = np.linspace(-1, 1, point_num, dtype=np.float32)   # x data

	# Test (1): Visualize a simple linear function with two parameters,
	# you can change LR to 1 to see the different pattern in gradient descent.
	print 'function=',function
	if function==1:
		y_fun = lambda a, b: a * x + b
		tf_y_fun = lambda a, b: a * x + b


	# Test (2): Using Tensorflow as a calibrating tool for empirical formula like following.
	if function==2:
		y_fun2 = lambda a, b, c : a * x**2 + b * x + c
		tf_y_fun2 = lambda a, b, c : a * x**2 + b * x + c


	# Test (3): Most simplest two parameters and two layers Neural Net, and their local & global minimum,
	# you can try different INIT_PARAMS set to visualize the gradient descent.
	if function==3:
		y_fun = lambda a, b: np.sin(a*np.cos(b*x))
		tf_y_fun = lambda a, b: tf.sin(a*tf.cos(b*x))

	noise = np.random.randn(point_num)/2
	if (function == 3):
			noise = noise/10
	if function==2:
		y = y_fun2(REAL_A,REAL_B,REAL_C) + noise         # target
		a, b = [tf.Variable(initial_value=p, dtype=tf.float32) for p in INIT_PARAMS]
		c = tf.Variable(initial_value=0,dtype=tf.float32)
		pred = tf_y_fun2(a, b,c)
	else:
		y = y_fun(REAL_A,REAL_B) + noise         # target
		a, b = [tf.Variable(initial_value=p, dtype=tf.float32) for p in INIT_PARAMS]
		print "a b", a, b
		pred = tf_y_fun(a, b)


	mse = tf.reduce_mean(tf.square(y-pred))
	train_op = tf.train.GradientDescentOptimizer(LR).minimize(mse)
	a_list, b_list,c_list ,cost_list = [], [], [],[]
	with tf.Session() as sess:
	    sess.run(tf.global_variables_initializer())
	    for t in range(iter_num):
	        a_, b_, mse_ = sess.run([a, b, mse])
	        a_list.append(a_); b_list.append(b_); cost_list.append(mse_)    # record parameter changes
	        c_list.append(sess.run(c) if function==2 else 0)
	        result, _ = sess.run([pred, train_op])                          # training
	a_list=np.array(a_list).tolist()
	b_list=np.array(b_list).tolist()
	c_list=np.array(c_list).tolist()
	cost_list=np.array(cost_list).tolist()

	# e1 = np.max(a_list)+np.max(a_list)-a_list[point_num-1]
	# s1 = e1-4*(np.max(a_list)-a_list[point_num-1])
	# e2 = np.max(b_list)+np.max(b_list)-b_list[point_num-1]
	# s2 = e2-4*(np.max(b_list)-b_list[point_num-1])
	# if s1>e1:
	# 	t = e1
	# 	e1 = s1
	# 	s1 = t
	# if s2>e2:
	# 	t = e2
	# 	e2 = s2
	# 	s2 = t
	ass = a_list[iter_num-1]-100
	ae = a_list[iter_num-1]+100
	bs = b_list[iter_num-1]-100
	be = b_list[iter_num-1]+100
	if function==3:
		ass = ass+80
		ae = ae-80
		bs = bs+80
		be = be-80
	# ran = np.linspace(s, e, point_num, dtype=np.float32)
	rana = np.linspace(ass, ae, 50, dtype=np.float32)
	ranb = np.linspace(bs, be, 50, dtype=np.float32)
	three_list = []
	if function==2:
		for a in rana:
			for b in ranb:
				three_list.append([a,b,np.mean((y_fun2(a,b,c_list[iter_num-1])-y)**2)])
	else:
		for a in rana:
			for b in ranb:
				three_list.append([a,b,np.mean((y_fun(a,b)-y)**2)])
	# print "&&&&&&&&&",three_list[0]
	return a_list,b_list,c_list,cost_list,x.tolist(),y.tolist(),result.tolist(),np.array(three_list).tolist()

def GradientDescentTest2(data,function=1,lr=0.01,init_params=[5, 1],iter_num=400):
	LR = lr
	INIT_PARAMS = init_params
					# [[5, 4],
	    #            [5, 1],
	    #            [2, 4.5]][1]
	#print '###########',data

	data=np.array(data,dtype=np.float32)

	x = [i for i in data[:,0].tolist()]
	y = [i for i in data[:,1].tolist()]        # target
	point_num = len(x)
	x = np.array(x)
	y = np.array(y)
	#print x
	#print y
	# Test (1): Visualize a simple linear function with two parameters,
	# you can change LR to 1 to see the different pattern in gradient descent.
	if function==1 :
		tf_y_fun = lambda a, b: a * x + b


	# Test (2): Using Tensorflow as a calibrating tool for empirical formula like following.
	if function==2:
		tf_y_fun2 = lambda a, b,c: a * x**2 + b * x + c


	# Test (3): Most simplest two parameters and two layers Neural Net, and their local & global minimum,
	# you can try different INIT_PARAMS set to visualize the gradient descent.
	if function==2:
		a, b = [tf.Variable(initial_value=p, dtype=tf.float32) for p in INIT_PARAMS]
		c = tf.Variable(initial_value=0,dtype=tf.float32)
		pred = tf_y_fun2(a, b,c)
	else:
		a, b = [tf.Variable(initial_value=p, dtype=tf.float32) for p in INIT_PARAMS]
		pred = tf_y_fun(a, b)
	# tensorflow graph

	mse = tf.reduce_mean(tf.square(y-pred))
	train_op = tf.train.GradientDescentOptimizer(LR).minimize(mse)

	a_list, b_list,c_list ,cost_list = [], [], [],[]
	with tf.Session() as sess:
	    sess.run(tf.global_variables_initializer())
	    for t in range(iter_num):
	        a_, b_, mse_ = sess.run([a, b, mse])
	        a_list.append(a_); b_list.append(b_); cost_list.append(mse_)    # record parameter changes
	        c_list.append(sess.run(c) if function==2 else 0)
	        result, _ = sess.run([pred, train_op])                          # training
	a_list=np.array(a_list).tolist()
	b_list=np.array(b_list).tolist()
	c_list=np.array(c_list).tolist()
	cost_list=np.array(cost_list).tolist()
	three_list = []

	# e1 = np.max(a_list)+np.max(a_list)-a_list[point_num-1]
	# s1 = e1-4*(np.max(a_list)-a_list[point_num-1])
	# e2 = np.max(b_list)+np.max(b_list)-b_list[point_num-1]
	# s2 = e2-4*(np.max(b_list)-b_list[point_num-1])
	# print s1,s2,e1,e2
	# if s1>e1:
	# 	t = e1
	# 	e1 = s1
	# 	s1 = t
	# if s2>e2:
	# 	t = e2
	# 	e2 = s2
	# 	s2 = t
	# e = np.max([e1,e2])
	# s = np.min([s1,s2])
	ass = a_list[iter_num-1]-100
	ae = a_list[iter_num-1]+100
	bs = b_list[iter_num-1]-100
	be = b_list[iter_num-1]+100
	# ran = np.linspace(s, e, point_num, dtype=np.float32)
	rana = np.linspace(ass, ae, 50, dtype=np.float32)
	ranb = np.linspace(bs, be, 50, dtype=np.float32)

	if function==2:
		for a in rana:
			for b in ranb:
				three_list.append([a,b,np.mean((tf_y_fun2(a,b,c_list[iter_num-1])-y)**2)])
	else:
		for a in rana:
			for b in ranb:
				three_list.append([a,b,np.mean((tf_y_fun(a,b)-y)**2)])
	return a_list,b_list,c_list,cost_list,x.tolist() ,y.tolist() ,result.tolist(),np.array(three_list).tolist()





# # visualization codes:

# print('a=', a_, 'b=', b_)
# plt.figure(1)
# plt.scatter(x, y, c='b')    # plot data
# plt.plot(x, result, 'r-', lw=2)   # plot line fitting

# # 3D cost figure
# fig = plt.figure(2); ax = Axes3D(fig)
# a3D, b3D = np.meshgrid(np.linspace(-2, 7, 30), np.linspace(-2, 7, 30))  # parameter space
# cost3D = np.array([np.mean(np.square(y_fun(a_, b_) - y)) for a_, b_ in zip(a3D.flatten(), b3D.flatten())]).reshape(a3D.shape)
# ax.plot_surface(a3D, b3D, cost3D, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'), alpha=0.5)
# ax.scatter(a_list[0], b_list[0], zs=cost_list[0], s=300, c='r')  # initial parameter place
# ax.set_xlabel('a'); ax.set_ylabel('b')
# ax.plot(a_list, b_list, zs=cost_list, zdir='z', c='r', lw=3)    # plot 3D gradient descent
# plt.show()
