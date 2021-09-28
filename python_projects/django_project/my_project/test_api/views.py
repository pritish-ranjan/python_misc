from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Student
from .serializers import StudentSerializer
from interfaces.fizzbuzz import Fizzbuzz

class StudentList(APIView):

    def __init__(self):
        self.fizzbuzz = Fizzbuzz()

    def get(self, request):
        print(request)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        print (request.data)
        num = request.data["number"]
        print(request.data["number"])
        response = self.fizzbuzz.calculate(num)

        return Response(data = response, status = status.HTTP_200_OK)
        # if request.method == "POST":
        #     data = request.POST.get("first_name", "lasst_name", "age")
        #     post_data = request.data
        #     print(post_data)
        #     post = Post()
        #     return Response(data = post_data, status = status.HTTP_202_ACCEPTED)

        
# Create your views here.
