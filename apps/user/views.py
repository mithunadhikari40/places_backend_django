from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from apps.user.serializers import UserSavedPlacesSerializer


class UserSavedPlacesView(GenericAPIView):
    serializer_class = UserSavedPlacesSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request, *args, **kwargs):

        try:
            user = request.user
            """Need to pass the user id along the request.data to the serializer, because it has a one to one 
            relationship with the user """
            request.data.update({'user': user.id})
            serializer = self.get_serializer(data=request.data)

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
