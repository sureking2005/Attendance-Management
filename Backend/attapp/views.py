from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['attendance']
teacher_collection = db['teacher']
student_collection = db['student']

@csrf_exempt
def teacher_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        id_number = data.get('id_number')
        password = data.get('password')

        if not (name and id_number and password):
            return JsonResponse({'message': 'Missing required fields'}, status=400)

        # Check if the teacher already exists
        if teacher_collection.find_one({'id_number': id_number}):
            return JsonResponse({'message': 'Teacher already registered'}, status=400)

        # Hash the password before saving
        hashed_password = generate_password_hash(password)
        teacher_collection.insert_one({
            'name': name,
            'id_number': id_number,
            'password': hashed_password
        })
        return JsonResponse({'message': 'Registration successful'})

    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def student_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        id_number = data.get('id_number')
        class_name = data.get('class_name')
        password = data.get('password')

        if not (name, id_number, class_name, password):
            return JsonResponse({'message': 'Missing required fields'}, status=400)

        # Check if the student already exists
        if student_collection.find_one({'id_number': id_number}):
            return JsonResponse({'message': 'Student already registered'}, status=400)

        # Hash the password before saving
        hashed_password = generate_password_hash(password)
        student_collection.insert_one({
            'name': name,
            'id_number': id_number,
            'class_name': class_name,
            'password': hashed_password
        })
        return JsonResponse({'message': 'Registration successful'})

    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def teacher_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_number = data.get('id_number')
        password = data.get('password')

        teacher = teacher_collection.find_one({'id_number': id_number})
        if teacher and check_password_hash(teacher['password'], password):
            return JsonResponse({'message': 'Teacher login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def student_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_number = data.get('id_number')
        password = data.get('password')

        student = student_collection.find_one({'id_number': id_number})
        if student and check_password_hash(student['password'], password):
            return JsonResponse({'message': 'Student login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'message': 'Invalid request method'}, status=405)