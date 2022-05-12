from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from apps.user.forms import UserSavedPlacesForm
from apps.user.serializers import UserSavedPlacesSerializer


class UserSavedPlacesView(GenericAPIView):
    serializer_class = UserSavedPlacesSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    # def perform_create(self, serializer):
    #     serializer.save(sender=self.request.user)

    def post(self, request, *args, **kwargs):

        try:
            user = request.user
            form = UserSavedPlacesForm(request.POST, request.FILES, instance=user)

            if form.is_valid():
                saved = form.save(commit=True)
                print(f"The saved value are {saved}")
                data = {
                    'message': 'Place saved successfully',
                    'data': form.data,
                    # 'token': token
                }
                return Response(data)
            else:
                return Response(form.errors)

        except BaseException as e:
            return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

# try:
#     serializer = self.get_serializer(data=request.data)
#     if serializer.is_valid():
#         saved = serializer.save()
#         print(f"The saved value are {saved}")
#         data = {
#             'message': 'User Created Successfully',
#             'data': serializer.data,
#             # 'token': token
#         }
#         return Response(data)
#     else:
#         return Response(serializer.errors)
#
# except BaseException as e:
#     return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
