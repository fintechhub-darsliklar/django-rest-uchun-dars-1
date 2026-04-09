from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Universitet
from .seralizers import UniversitetSeralizer

# Create your views here.


class UniversitetApiView(APIView):

    def get(self, request):
        universitetlar = Universitet.objects.all()
        data = UniversitetSeralizer(universitetlar, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = UniversitetSeralizer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
