from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from .pagination import *



@api_view(['GET'])
def index (request):
    person1 = {
        "name":"shakin",
        "age":18,
        "is_marride":False,
    }
    person2 = {
        "name":"shakin",
        "age":18,
        "is_marride":False,
    }
    

    person_list = [person1,person2]

    return Response(person_list)


@api_view(['GET','POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        
        paginator = TodoPagination()
        page = paginator.paginate_queryset(todos, request)


        serializer = TodoListSeializer(todos, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        data = request.data
        serializer = TodoDetailSeializer(data=data)
        if serializer.is_valid():
            serializer.save(create_by = request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def todo_detail(request,id):
    todo = get_object_or_404(Todo, id=id)
    serializer = TodoDetailSeializer(todo)
    return Response(serializer.data)
    

