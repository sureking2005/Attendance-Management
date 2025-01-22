from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import rest_framework
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate




@csrf_exempt
def teacher_login(request):
    if request.method=='POST':
        data=json.loads(request.body)
        id_number = data.get['id_number']
        password = data.get['password']
        teacher = authenticate(request, id_number=id_number, password=password)
        if teacher is not None:
            return JsonResponse({'message': 'Teacher login successful'})
        else:    
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'message':'Inavlid request method'},status=405)

@csrf_exempt
def student_login(request):
    if request.method=='POST':
        data=json.loads(request.body)
        id_number = data.get['id_number']
        password = data.get['password']
        student = authenticate(request, id_number=id_number, password=password)
        if student is not None:
            return JsonResponse({'message': 'Student login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    return JsonResponse({'message':'Inavlid request method'},status=405)

@csrf_exempt
def parent_login(request):
    if request.method=='POST':
        data=json.loads(request.body)

        return JsonResponse({'message':'Login Successful'})
    return JsonResponse({'message':'Inavlid request method'},status=405)


@csrf_exempt
def teacher_register(request):
    if request.method=='POST':
        data=json.loads(request.body)
        return JsonResponse({'message':'Registration Successful'})
    return JsonResponse({'message':'Inavlid request method'},status=405)

@csrf_exempt
def student_register(request):
    if request.method=='POST':
        data=json.loads(request.body)
        return JsonResponse({'message':'Registration Successful'})
    return JsonResponse({'message':'Inavlid request method'},status=405)

