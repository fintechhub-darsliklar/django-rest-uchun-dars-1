from rest_framework.serializers import ModelSerializer
from .models import Universitet, Group, Student, Teacher


class UniversitetSeralizers(ModelSerializer):

    class Meta:
        model = Universitet
        fields = ['id', 'name', 'is_active', 'address']



class TeacherSeralizers(ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"


class StudentSeralizers(ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class GroupSeralizers(ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"