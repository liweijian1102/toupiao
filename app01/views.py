#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.http import  HttpResponse
from django.template.context import RequestContext
import models
from django.contrib import auth
from django.http.response import HttpResponseRedirect
# Create your views here.
def login(request):
    return render_to_response('login.html')

def acc_login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=auth.authenticate(username=username,password=password)
    print username,password,user
    if user is not None:
        print '------------------'
        auth.login(request,user)
        print user
        return render_to_response('vote.html',{'user':request.user})
    else:
        return render_to_response('login.html',context_instance=RequestContext(request))

def vote(request):
    return render_to_response('vote.html')
def vote_tab(request):
    return render_to_response('vote_tab.html',{'user':request.user})
def vote_create(request):
    return render_to_response('vote_create.html')

def vote_tab_add(request):
    vote_title=request.POST.get('vote_title')
    vote_start=request.POST.get('vote_start')
    vote_end=request.POST.get('vote_end')
    models.vote.objects.create(
        vote_title=vote_title,
        vote_start=vote_start,
        vote_end=vote_end,
        vote_zuozhe=request.user
        )
    print '--------------------'
    print vote_title,vote_start,vote_end
    return HttpResponseRedirect('/vote_create')

    
def vote_content_single(request):
    vote_content_list=models.vote_content.objects.all()
    vote=models.vote.objects.all()

    
    return render_to_response('vote_content_single.html',{'user':request.user,'content_list':vote_content_list,'vote':vote})


def vote_single_add(request):
    vote_bt=request.POST.get('vote_bt')
    vote_a=request.POST.get('vote_a')
    vote_b=request.POST.get('vote_b')
    vote_c=request.POST.get('vote_c')
    vote_d=request.POST.get('vote_d')
    vote_e=request.POST.get('vote_e')
    vote_f=request.POST.get('vote_f')
    vote_tit=request.POST.get('tit')
    print vote_bt,vote_a,vote_b,vote_tit
    models.vote_content.objects.create(
        vote_bt=vote_bt,
        vote_a=vote_a,
        vote_b=vote_b,
        vote_c=vote_c,
        vote_d=vote_d,
        vote_e=vote_e,
        vote_f=vote_f,
        vote_tit=vote_tit,
        vote_type="1",
        content_zuozhe=request.user
        )
    
    return render_to_response('vote_content_single.html')
    
    
def vote_content_double(request):
    pass
def vote_content_tex(request):
    pass
    