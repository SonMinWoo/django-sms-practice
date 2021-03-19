from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import requests, json
import datetime
from django.utils import timezone
from random import randint


# Create your views here.

URL = "https://apis.aligo.in/send/"
auth_db = {}

@csrf_exempt
def auth_post(request):

    if request.method == 'POST':
        req_data = JSONParser().parse(request)
        global URL
        headers = {}
        auth_number = randint(1000, 10000)
        data = {
            "key" : "",
            "user_id" : "",
            "sender" : "",
            "receiver" : req_data['phone_number'],
            "msg" : "발신번호는 {}입니다.".format(auth_number)
        }
        res = requests.post(URL, headers=headers, data=data)
        auth_db[req_data['phone_number']] = auth_number
        print(json.loads(res.text))

        return HttpResponse(status=200)

@csrf_exempt
def verify_post(request):

    if request.method == 'POST':
        req_data = JSONParser().parse(request)
        print(auth_db)
        print(auth_db[req_data['phone_number']])
        print(req_data)
        if str(auth_db[req_data['phone_number']]) == str(req_data['verify_number']):
            del(auth_db[req_data['phone_number']])
            return HttpResponse("True",status=200)
        else:
            return HttpResponse("False",status=200)