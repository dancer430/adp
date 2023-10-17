from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect, StreamingHttpResponse
from django.contrib.auth import authenticate
from appointment.models import AppointmentRecord


def menu_html(request):
    """
    主菜单页面跳转
    :param request:
    :return:
    """
    return render(request, 'appointment/menu.html', {})


def appointment_html(request):
    """
    跳转预约查看界面
    :param request:
    :return:
    """
    return render(request, 'appointment/appointment.html', {})


# Create your views here.
def appointment_list(request):
    """
    查看预约列表信息
    """
    try:
        operator_id = request.session.get('userid')
        start_time = request.GET.get('date')
        print(operator_id)
        print(start_time)
        _ret = []
        appointments = AppointmentRecord.objects.filter(docker_id=operator_id, start_time__gt=start_time).order_by("start_time")
        for i in appointments:
            _dict = {
                'id': i.id,
                'doctor': i.docker.username,
                'patient': i.patient.username,
                'start_time': str(i.start_time),
                'end_time': str(i.end_time),
                'register': i.operator_user.username,
                'status': i.status.message
            }
            _ret.append(_dict)

        return JsonResponse({"meta": {"msg": "更新成功！", "status": 200}, "data": _ret})
    except Exception as e:
        return JsonResponse({"meta": {"msg": "操作失败, 请联系管理员！", "status": 201}, "data": str(e)})


def appointment_operation(request):
    """
    预约操作
    """
    try:
        return JsonResponse({"meta": {"msg": "登录成功！", "status": 200}, "data": ""})
    except Exception as e:
        return JsonResponse({"meta": {"msg": "登录失败！", "status": 201}, "data": ""})


def logout(request):
    """
    登出操作
    """
    try:
        auth.logout(request)
        return JsonResponse({"meta": {"msg": "登出成功！", "status": 200}, "data": ""})
    except Exception as e:
        return JsonResponse({"meta": {"msg": "登出失败！", "status": 201}, "data": str(e)})
