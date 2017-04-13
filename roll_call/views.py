from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from roll_call.models import set_time,set_number,attendence
from django.utils import timezone

import random
from datetime import datetime

# Create your views here.

def produce_three_number(request):

	time=set_time.objects.latest('start')
	d = timezone.now()
	if time.start <= d <= time.end:
		random.seed(a=d.day)
		num_set = [ i for i in range(1000)]
		random.shuffle(num_set)
		num_1, num_2, num_3 = num_set[:3]
		return render_to_response("roll_call/roll_call.html", locals())
	else:
		return HttpResponse("未開放點名")

def roll_call(request):
    if request.user.is_authenticated() and request.method == "POST" and request.POST['answer']:
        if request.user.is_superuser:
            num = set_number(number = request.POST['answer'])
            num.save()
            return HttpResponse("成功輸入正確點名號碼")
        else:
            try:
                set_num = set_number.objects.latest('created_date')
                if set_num.created_date.day != timezone.now().day:
                    return HttpResponse("老師未開始點名")
            except:
                    return HttpResponse("老師未開始點名")
            num = set_num.number
            if 'answer' in request.POST:
                if int(request.POST['answer']) == num :
                    result = attendence(attend="OK", student = request.user.username)
                    result.save()
                    return HttpResponse("已點名")
                else:
                    result = attendence(attend=False, student = request.user.username)
                    result.save()
                    print("num", num)
                    print("post: ", request.POST['answer'])
                    return HttpResponse("未成功點名")
    return redirect('/')



