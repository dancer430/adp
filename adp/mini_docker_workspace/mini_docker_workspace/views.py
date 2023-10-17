"""
common_views
"""
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect, StreamingHttpResponse
from django.contrib.auth import authenticate


def login_html(request):
    """
    登陆页面跳转
    :param request:
    :return:
    """
    return render(request, 'index.html', {})


def do_login(request):
    loginer = authenticate(username=request.GET.get('username'),
                           password=request.GET.get('password'))
    if loginer is not None:
        request.session['userid'] = loginer.id
        request.session['realname'] = loginer.first_name
        request.session['username'] = request.GET.get('username')
        request.session.set_expiry(24 * 60 * 60 * 1000)
        request.session.save()
        return JsonResponse({"meta": {"msg": "登录成功！", "status": 200}, "data": ""})
    else:
        return JsonResponse({"meta": {"msg": "登录失败！", "status": 201}, "data": ""})