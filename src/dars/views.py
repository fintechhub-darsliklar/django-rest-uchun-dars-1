from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .seralizers import UniversitetSeralizers, StudentSeralizers, GroupSeralizers, TeacherSeralizers
from .models import Universitet, Student, Group, Teacher


class UniversitetApiView(APIView):
    
    def get(self, request):
        universitets = Universitet.objects.all()
        data = UniversitetSeralizers(universitets, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = UniversitetSeralizers(data=request.data)
        if data.is_valid(raise_exception=True):
            data.save()
        return Response(data.data, status=status.HTTP_201_CREATED)


class StudentApiView(APIView):
    
    def get(self, request):
        students = Student.objects.all()
        data = StudentSeralizers(students, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = StudentSeralizers(data=request.data)
        if data.is_valid(raise_exception=True):
            data.save()
        return Response(data.data, status=status.HTTP_201_CREATED)
    

class GroupApiView(APIView):
    
    def get(self, request):
        groups = Group.objects.all()
        data = GroupSeralizers(groups, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = GroupSeralizers(data=request.data)
        if data.is_valid(raise_exception=True):
            data.save()
        return Response(data.data, status=status.HTTP_201_CREATED)
    

class TeacherApiView(APIView):
    
    def get(self, request):
        teachers = Teacher.objects.all()
        data = TeacherSeralizers(teachers, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = TeacherSeralizers(data=request.data)
        if data.is_valid(raise_exception=True):
            data.save()
        return Response(data.data, status=status.HTTP_201_CREATED)
