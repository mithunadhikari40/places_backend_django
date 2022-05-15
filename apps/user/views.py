from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from apps.user.models import UserSavedPlacesModel
from apps.user.serializers import UserSavedPlacesSerializer
from rest_framework import viewsets, status
from rest_framework import viewsets, status


class UserSavedPlacesView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    """When we annotate a method with staticmethod, the first argument self will not be there, if we
    were to remove this annotation, self should be added as the first argument to the enclosing function"""

    @staticmethod
    def retrieve(request, pk=None):
        if pk is None:
            return Response({'error': f'Id is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            place = UserSavedPlacesModel.objects.get(id=pk)
            if place:
                serializer = UserSavedPlacesSerializer(place)
                return Response({'place': serializer.data}, status=status.HTTP_200_OK)
            return Response({'error': f'No place found with id of {pk}'}, status=status.HTTP_404_NOT_FOUND)

        except BaseException as e:
            return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def list(request):
        try:
            places = UserSavedPlacesModel.objects.all()
            if places:
                serializer = UserSavedPlacesSerializer(places, many=True)
                return Response({'place': serializer.data}, status=status.HTTP_200_OK)
            return Response({'error': f'No places found with id of'}, status=status.HTTP_404_NOT_FOUND)

        except BaseException as e:
            return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def create(request):
        try:
            user = request.user
            """Need to pass the user id along the request.data to the serializer, because it has a one to one 
            relationship with the user """
            request.data.update({'user': user.id})
            serializer = UserSavedPlacesSerializer(data=request.data)

            if serializer.is_valid():
                saved = serializer.save()
                print(f"The saved value are {saved}")
                data = {
                    'message': 'Place saved successfully',
                    'data': serializer.data,
                    # 'token': token
                }
                return Response(data)
            else:
                return Response(serializer.errors)

        except BaseException as e:
            return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
