from reviewSystem.models import Item,Category,User,Rating
from reviewSystem.serializers import ItemSerializer,CategorySerializer,UserSerializer,RatingSerializer
#from django.shortcuts import render
#from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication  ?? check
# below line for user privilege
# from django.contrib.auth.models import User


# these are generic views
# Create your views here.



class ItemDetails(APIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    def get(self, request, format=None):
        item = Item.objects.all() #here  Item is the model
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer=ItemSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    		


class ItemEdit(APIView):
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CategoryDetails(APIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    def get(self, request, format=None):
        category = Category.objects.all() #here  Category is the model
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)		

class UserDetails(APIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    def get(self, request, format=None):
        user = User.objects.all() #here  User is the model
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class UserEdit(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#use of generic  class based views LISTAPIVIEWS and RETRIEVEAPIVIEWS
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = RootUserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = RootUserSerializer
