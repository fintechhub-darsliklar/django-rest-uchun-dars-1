from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .seralizers import TodoListSeralizer
from .models import TodoList
# Create your views here.

class TodoListApiView(APIView):
    
    def get(self, request, pk=None):
        todolists = TodoList.objects.all()
        data = TodoListSeralizer(todolists, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = TodoListSeralizer(data=request.data)
        if data.is_valid(raise_exception=True):
            data.save()
        return Response(data.data, status=status.HTTP_201_CREATED)


    def patch(self, request, pk=None):
        if pk:
            todo = TodoList.objects.get(id=pk)
            data = TodoListSeralizer(data=request.data, instance=todo, partial=True)
            if data.is_valid(raise_exception=True):
                data.save()
            return Response(data.data, status=status.HTTP_202_ACCEPTED)

        return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
    

