from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.favorites.models import FavoriteModel
from apps.favorites.serializers import FavoriteSerializer


class FavoriteView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def create(request):
        try:
            user = request.user
            request.data.update({'user': user.id})
            favorite_item = request.data.get('favorite', None)
            if not favorite_item:
                return Response({'error': 'Favorite item id is required'}, status=status.HTTP_400_BAD_REQUEST)
            filters = {'user': user.id, 'favorite': favorite_item}

            item = FavoriteModel.objects.filter(**filters)
            if item is None:
                return Response({'error': f'The place with id of {favorite_item} does not exits.'},
                                status=status.HTTP_400_BAD_REQUEST)

            if len(item) == 1:
                item.delete()
                data = {
                    'message': 'Place deleted from favorites successfully',
                }
                return Response(data)
            print(f"The request data is {request.data}")
            serializer = FavoriteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = {
                    'message': 'Place added to favorite successfully',
                    'data': serializer.data
                }
                return Response(data)
                pass
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except BaseException as e:
            return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def retrieve(request, pk=None):
        if pk is None:
            return Response({'error': f'Id is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            place = FavoriteModel.objects.get(id=pk)
            print(f"The user is this {request.user.id} and place is {place.user}")
            if place:
                serializer = FavoriteSerializer(place)
                return Response({'places': serializer.data}, status=status.HTTP_200_OK)

            return Response({'error': f'No place found with id of {pk}'}, status=status.HTTP_404_NOT_FOUND)

        except BaseException as e:
            return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def destroy(request, pk=None):
        if pk is None:
            return Response({'error': f'Id is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            place = FavoriteModel.objects.get(id=pk)
            if place:
                if place.user.id == request.user.id:
                    place.delete()
                    return Response({'message': 'Place deleted successfully'}, status=status.HTTP_200_OK)
                return Response({'error': f'You do not have permission to delete this item'},
                                status=status.HTTP_403_FORBIDDEN)
            return Response({'error': f'No place found with id of {pk}'}, status=status.HTTP_404_NOT_FOUND)

        except BaseException as e:
            return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def list(request):
        try:
            places = FavoriteModel.objects.all()
            if places:
                serializer = FavoriteSerializer(places, many=True)
                print(f"The serializer data is this one {serializer.data}")
                return Response({'places': serializer.data}, status=status.HTTP_200_OK)
            return Response({'error': f'No places found with id of'}, status=status.HTTP_404_NOT_FOUND)

        except BaseException as e:
            return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def partial_update(request, pk=None):
        if pk is None:
            return Response({'error': f'Id is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            place = FavoriteModel.objects.get(id=pk)
            if place:
                if place.user.id == request.user.id:
                    serializer = FavoriteSerializer(place, data=request.data, partial=True)
                    if serializer.is_valid():
                        serializer.save()

                        return Response({'message': 'Place updated successfully', 'data': serializer.data},
                                        status=status.HTTP_200_OK)
                return Response({'error': f'You do not have permission to update this item'},
                                status=status.HTTP_403_FORBIDDEN)
            return Response({'error': f'No place found with id of {pk}'}, status=status.HTTP_404_NOT_FOUND)

        except BaseException as e:
            return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
