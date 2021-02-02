from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)



@api_view(['GET'])
def taskDetail(request , pk):
    tasks = get_object_or_404(Task,id=pk)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    
    serializer = TaskSerializer(data = request.data)

    if( serializer.is_valid()):
        serializer.save() 

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request,pk):
    task = get_object_or_404(Task,id=pk) #find that id and then update it
    
    serializer = TaskSerializer(instance=task ,data = request.data)

    if( serializer.is_valid()):
        serializer.save() 

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request,pk):
    task = get_object_or_404(Task,id=pk) #find that id and then update it
    task.delete()

    return Response("item have been deleted! ")