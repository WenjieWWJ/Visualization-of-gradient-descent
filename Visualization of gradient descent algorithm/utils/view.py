# -*- coding: utf-8 -*-
# from django.http import HttpResponse
 
# def hello(request):
#     return HttpResponse("Hello world ! ")

from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World !'
    return render(request, 'hello.html', context)

from django.http import HttpResponse
from django.shortcuts import render_to_response

# 表单
def search_form(request):
    return render_to_response('search_form.html')

# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = 'the content: ' + request.GET['q']
    else:
        message = 'empty sheet'
    return HttpResponse(message)
