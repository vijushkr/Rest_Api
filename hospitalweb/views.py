from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status 
from hospitalweb.models import Users
from hospitalweb.serializers import UsersSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def users_list(request):
    # GET list of users, POST a new user, DELETE  user
    if request.method == 'GET':
        users = Users.objects.all() 
               
        users_serializer = UsersSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # 'safe=False' for objects serialization
        
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def user_detail(request, pk):
    # find user by pk (id)
    user = Users.objects.get(pk=pk)
    if request.method == 'GET': 
        user_serializer = UsersSerializer(user) 
        return JsonResponse( user_serializer.data) 
    elif request.method == 'PUT': 
         user_data = JSONParser().parse(request) 
         user_serializer = UsersSerializer(user, data=user_data) 
         if user_serializer.is_valid(): 
              user_serializer.save() 
              return JsonResponse(user_serializer.data) 
         return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
       user.delete()
       return JsonResponse({'message': 'User was deleted successfully!'}, 
        status=status.HTTP_204_NO_CONTENT
        )

def user_delete(request, pk):
    # find product by pk (id)
    user = Users.objects.get(pk=pk)


