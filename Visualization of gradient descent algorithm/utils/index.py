# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import json
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from tf_gd import GradientDescentTest1
from tf_gd import GradientDescentTest2

# 接收POST请求数据
def post(request):
	ctx = {}
	if request.POST:
		print request.POST
		if request.POST['type']=='test1':
			ctx['iter_num'] = request.POST['iter_num']
			ctx['learning_rate'] = request.POST['learning_rate']
			ctx['function'] = request.POST['function']
			ctx['init_params_a'] = float(request.POST['init_params_a'].decode("utf-8").encode("gbk"))
			ctx['init_params_b'] = float(request.POST['init_params_b'].decode("utf-8").encode("gbk"))
			ctx['arg'] = json.loads(request.POST['arg'])
			print ctx['arg']
			res = processTest1(ctx)
		elif request.POST['type']=='test2':
			ctx['select_model'] = request.POST['select_model']
			ctx['iter_num'] = request.POST['iter_num']
			ctx['learning_rate'] = request.POST['learning_rate']
			ctx['data'] = json.loads(request.POST['dataArray'])['dataArray']
			ctx['init_params_a'] = float(request.POST['init_params_a'].decode("utf-8").encode("gbk"))
			ctx['init_params_b'] = float(request.POST['init_params_b'].decode("utf-8").encode("gbk"))
			res = processTest2(ctx)
		return HttpResponse(res, content_type='application/json')

	return render(request, "index.html")


def processTest1(ctx):

	res={}
	arg = ctx['arg']
	iter_num = int(ctx['iter_num'])
	learning_rate = float(ctx['learning_rate'])
	init_params_a = ctx['init_params_a']
	init_params_b = ctx['init_params_b']
	print '****',arg
	if arg[0]!=0:
		a_list,b_list,c_list,cost_list,x_list,y_list,results_list,three_list=GradientDescentTest1(function=arg[0],lr=learning_rate,real_params=arg[1:4],init_params=[init_params_a,init_params_b],iter_num=iter_num,point_num=30)
		#a_list,b_list,c_list,cost_list,x_list,y_list,results_list=GradientDescentTest1(function=arg[0],lr=learning_rate,real_params=arg[1:4],init_params=[1,1],iter_num=iter_num,point_num=30)
		res['state']='success'
		res['func']=arg[0]
		res['a_list'] = a_list
		res['b_list'] = b_list
		res['c_list'] = c_list
		res['cost_list'] = cost_list
		res['x_list'] = x_list
		res['y_list'] = y_list
		res['results_list'] = results_list
		res['graph_3d'] = three_list
	else:
		res['state']='fail'
		res['reason']='the format of function is incorrect!'


	return json.dumps(res)
def processTest2(ctx):

	res={}
	iter_num = int(ctx['iter_num'])
	learning_rate = float(ctx['learning_rate'])
	if ctx['select_model'] == 'linear regression':
		select_model = 1
	else:
		select_model = 2
	data = ctx['data']
	print select_model
	init_params_a = ctx['init_params_a']
	init_params_b = ctx['init_params_b']
	a_list,b_list,c_list,cost_list,x_list,y_list,results_list,three_list=GradientDescentTest2(data = data,function=select_model,lr=learning_rate,init_params=[init_params_a,init_params_b],iter_num=iter_num)
	#a_list,b_list,c_list,cost_list,x_list,y_list,results_list=GradientDescentTest2(data = data,function=select_model,lr=learning_rate,init_params=[1,1],iter_num=iter_num)
	res['state']='success'
	res['func']=select_model;
	res['a_list'] = a_list
	res['b_list'] = b_list
	res['c_list'] = c_list
	res['cost_list'] = cost_list
	res['x_list'] = x_list
	res['y_list'] = y_list
	res['results_list'] = results_list
	res['graph_3d'] = three_list
	return json.dumps(res)
