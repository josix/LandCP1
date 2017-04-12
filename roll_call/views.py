from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

import random
from datetime import datetime

# Create your views here.

def produce_three_number(request):
    d = datetime.now()
    if 9 <= d.hour <= 11:
        random.seed(a=d.day)
        num_set = [ i for i in range(1000)]
        random.shuffle(num_set)
        num_1, num_2, num_3 = num_set[:3]
        return render_to_response("roll_call/roll_call.html", locals())
    else:
        return HttpResponse("未開放點名")
