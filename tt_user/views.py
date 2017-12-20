# coding=utf-8
from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from hashlib import sha1

# 注册页面
def register(request):
    return render(request, 'tt_user/register.html', {'title': '注册'})


# 处理注册
def register_handle(request):
    # 接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    cpwd = post.get('cpwd')
    uemail = post.get('email')
    # 判断两次密码是否相等
    if upwd != cpwd:
        return redirect('/user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    pwd = s1.hexdigest()

    # 创建对象
    user = models.UserInfo()
    user.uname = uname
    user.upwd = pwd
    user.uemail = uemail
    user.save()
    return redirect('/user/login')


# 判断用户名是否已经存在
def register_exists(request):
    username = request.GET.get('uname')
    count = models.UserInfo.objects.filter(uname=username).count()
    return JsonResponse({'count': count})


# 登录
def login(request):
    username = request.COOKIES.get('username', '')
    return render(request, 'tt_user/login.html', {'title': '登录', 'username':username})


# 登录处理
def login_handle(request):
    # 获取用户输入
    post = request.POST
    username = post.get('username')
    userpwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)
    user = models.UserInfo.objects.filter(uname=username)
    if len(user) == 1:
        # 密码加密
        s1 = sha1()
        s1.update(userpwd.encode('utf-8'))
        userpwd1 = s1.hexdigest()
        if user[0].upwd == userpwd1:
            # 用户名密码都正确,跳转到用户中心
            red = HttpResponseRedirect('/user/info')
            # 如勾选了记住用户名,设置cookie和session信息
            if jizhu != 0:
                red.set_cookie('username', username)
            else:
                red.set_cookie('username', '', max_age=-1)
            request.session['user_id'] = user[0].id
            request.session['username'] = username
            return red
        else:
            # 密码错误
            context = {'title': '登录', 'error_name': 0, 'error_password': 1, 'username': username, 'userpwd': userpwd}
            return render(request, 'tt_user/login.html', context)
    else:
        # 用户名错误
        context = {'title': '登录', 'error_name': 1, 'error_password': 0, 'username': username, 'userpwd': userpwd}
        return render(request, 'tt_user/login.html', context)


# 用户中心－个人信息
def info(request):
    user_id = request.session['user_id']
    user_email = models.UserInfo.objects.get(pk=user_id).uemail
    context = {
        'title': '用户中心',
        'user_email': user_email,
        'user_name': request.session['username']
    }
    return render(request, 'tt_user/user_center_info.html', context)


# 用户中心－全部订单
def order(request):
    user_id = request.session['user_id']
    user_email = models.UserInfo.objects.get(pk=user_id).uemail
    context = {
        'title': '用户中心',
        'user_email': user_email,
        'user_name': request.session['username'],

    }
    return render(request, 'tt_user/user_center_order.html', context)


# 用户中心－收货地址
def site(request):
    user = models.UserInfo.objects.get(pk=request.session['user_id'])
    user_id = request.session['user_id']
    user_email = models.UserInfo.objects.get(pk=user_id).uemail
    context = {
        'title': '用户中心',
        'user_email': user_email,
        'user_name': request.session['username'],
        'user': user
    }
    return render(request, 'tt_user/user_center_site.html', context)


def site_handle(request):
    user = models.UserInfo.objects.get(pk=request.session['user_id'])
    if request.method=='POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddr = post.get('uaddr')
        user.upostcode = post.get('upostcode')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title': '用户中心', 'user': user}
    return render(request, 'tt_user/user_center_site.html', context)
