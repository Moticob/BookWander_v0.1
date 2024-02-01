from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.http import Http404


class UsersApi(APIView): 
    """
        
    """
    sc = UserSerializer

    def get(self, request):
        users = User.objects.all()
        s = self.sc(users, many=True)
        #status=status.HTTP_200_OK
        return Response(s.data)
    
class UserApi(APIView):
    """
        
    """
    sc = UserSerializer
    def get(self, request, id):
        try:
            user = User.objects.get(user_id=id)
        except User.DoesNotExist:
            raise Http404("Given query not found....")
        s = self.sc(user)
        return Response(s.data)
    def put(self, request, id):
        try:
            user = User.objects.get(user_id=id)
        except User.DoesNotExist:
            raise Http404("Given query not found....")
        s = self.sc(instance=user, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            user = User.objects.get(user_id=id)
        except User.DoesNotExist:
            raise Http404("Given query not found....")
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCreateApi(APIView):
    """
        
    """
    sc = UserSerializer
    def post(self, request):
        s = self.sc(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)