from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from medbayapi.serializers import UserSerializer
from medbayapi.models import User

class UserView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single user
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """"Handle GET requests for all users"""
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized user instance
        """
        user = User.objects.create(
            name=request.data['name'],
            age=request.data['age'],
            bio=request.data['bio'],
            image_url=request.data['image_url'],
            email=request.data['email'],
            location=request.data['location'],
            local_pharmacy=request.data['local_pharmacy'],
        )
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a user

        Returns:
            Response -- Empty body with 204 status code
        """

        user = User.objects.get(pk=pk)
        user.name=request.data['name']
        user.age=request.data['age']
        user.bio=request.data['bio']
        user.image_url=request.data['image_url']
        user.email=request.data['email']
        user.location=request.data['location']
        user.local_pharmacy=request.data['local_pharmacy']
        user.save()


        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all users"""
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
