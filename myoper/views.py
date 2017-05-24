#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import T_USER
from django import forms
from flask.wrappers import Response
# Create your views here.
def index(request):
    return HttpResponse("Rango says hey there partner!")

class UserFrom(forms.Form):
    user_id=forms.CharField(label="用户编号",max_length=8)
    user_password=forms.CharField(label="密码",widget=forms.PasswordInput,max_length=10)
def login(request):
    if request.method=='POST':
        form=UserFrom(request.POST)
        if form.is_valid():  #提交的数据合法
            user_id=form.chended_data['user_id']
            user_password=form.chended_data['user_password']
            user = T_USER.objects.filter(user_id__excat=user_id,user_password__excat=user_password,
            user_status__excat='0')
            if user:#假如用户名密码和状态正确开始跳转
                response=HttpResponseRedirect('/index')
                response.set_cookie('user_id', user_id, 3600)
                return response
            else:
                return HttpResponseRedirect('login')
        else:
            from=UserFrom()