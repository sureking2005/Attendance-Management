from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

client = MongoClient('mongodb://localhost:27017/')
db = client['attendance']
teacher_collection = db['teacher']
student_collection = db['student']
attendance_collection = db['attendance_details']

def validate_login_fields(data, required_fields):
    missing_fields = [field for field in required_fields if not data.get(field)]
    if missing_fields:
        return f"Missing required fields: {', '.join(missing_fields)}"
    return None

@csrf_exempt
def teacher_register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            id_number = data.get('id_number')
            password = data.get('password')

            if not (name and id_number and password):
                return JsonResponse({'message': 'Missing required fields'}, status=400)

            if teacher_collection.find_one({'id_number': id_number}):
                return JsonResponse({'message': 'Teacher already registered'}, status=400)

            hashed_password = generate_password_hash(password)
            teacher_collection.insert_one({
                'name': name,
                'id_number': id_number,
                'password': hashed_password
            })
            return JsonResponse({'message': 'Teacher registration successful'})
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def student_register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            id_number = data.get('id_number')
            class_name = data.get('class_name')
            password = data.get('password')
            if not (name and id_number and class_name and password):
                return JsonResponse({'message': 'Missing required fields'}, status=400)
            if student_collection.find_one({'id_number': id_number}):
                return JsonResponse({'message': 'Student already registered'}, status=400)
            hashed_password = generate_password_hash(password)
            student_collection.insert_one({
                'name': name,
                'id_number': id_number,
                'class_name': class_name,
                'password': hashed_password
            })
            return JsonResponse({'message': 'Student registration successful'})
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def teacher_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            error_message = validate_login_fields(data, ['id_number', 'password'])
            if error_message:
                return JsonResponse({'message': error_message}, status=400)
            id_number = data['id_number']
            password = data['password']
            teacher = teacher_collection.find_one({'id_number': id_number})
            if teacher and check_password_hash(teacher['password'], password):
                return JsonResponse({'message': 'Teacher login successful', 'name': teacher['name']})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def student_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)            
            error_message = validate_login_fields(data, ['id_number', 'password'])
            if error_message:
                return JsonResponse({'message': error_message}, status=400)
            id_number = data['id_number']
            password = data['password']
            student = student_collection.find_one({'id_number': id_number})
            if student and check_password_hash(student['password'], password):
                return JsonResponse({'message': 'Student login successful', 'name': student['name']})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def save_attendance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_number = data.get('id_number')  # Changed from teacher_id to id_number
            date = data.get('date')
            attendance_records = data.get('attendance_records')

            if not id_number:
                return JsonResponse({'message': 'Teacher ID (id_number) is missing'}, status=400)
            if not date:
                return JsonResponse({'message': 'Date is missing'}, status=400)
            if not attendance_records:
                return JsonResponse({'message': 'Attendance records are missing'}, status=400)

            attendance_doc = {
                'id_number': id_number,  # Store id_number in attendance
                'date': date,
                'attendance_records': attendance_records
            }
            attendance_collection.insert_one(attendance_doc)
            return JsonResponse({'message': 'Attendance saved successfully'})
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    return JsonResponse({'message': 'Invalid request method'}, status=405)
