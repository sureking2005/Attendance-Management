from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import rest_framework

@csrf_exempt
def teacher_login(request):
    if request.method=='POST':
        data=json.loads(request.body)

        return JsonResponse({'message': 'Teacher login successful'})
    return JsonResponse({'message':'Inavlid request method'},status=405)
#command
@csrf_exempt
def student_login(request):
    if request.method=='POST':
        data=json.loads(request.body)

        return JsonResponse({'message':'Login Successful'})
    return JsonResponse({'message':'Inavlid request method'},status=405)

@csrf_exempt
def parent_login(request):
    if request.method=='POST':
        data=json.loads(request.body)

        return JsonResponse({'message':'Login Successful'})
    return JsonResponse({'message':'Inavlid request method'},status=405)
