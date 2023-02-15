from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from medbayapi.models import Physician, Record, User, PhysicianUser
from medbayapi.serializers import PhysicianSerializer
from rest_framework.decorators import action

class PhysicianView(ViewSet):

    def retrieve(self, request, pk):
        physician = Physician.objects.get(pk=pk)
        serializer = PhysicianSerializer(physician)
        return Response(serializer.data)

    def list(self, request):
        physicians = Physician.objects.all()

        serializer = PhysicianSerializer(physicians, many=True)
        return Response(serializer.data)


    def create(self, request):
        """Handle create requests for physician
        """
        record = Record.objects.get(pk=request.data["record"])
        user = User.objects.get(pk=request.data["user"])

        physician = Physician.objects.create(
                name=request.data["name"],
                specialty=request.data["specialty"],
                email=request.data["email"],
                location=request.data["location"],
                phone_number=request.data["phone_number"],
                record=record,
                user=user
            )
        serializer = PhysicianSerializer(physician)
        return Response(serializer.data)

    def update(self, request, pk):

        physician = Physician.objects.get(pk=pk)
        physician.name=request.data["name"]
        physician.specialty=request.data["specialty"]
        physician.email=request.data["email"]
        physician.location=request.data["location"]
        physician.phone_number=request.data["phone_number"]

        record = Record.objects.get(pk=request.data["record"])
        physician.record=record
        physician.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        physician = Physician.objects.get(pk=pk)
        physician.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def assign(self, request, pk):
        """Post request for a user to sign up for an physician"""

        physician = Physician.objects.get(pk=pk)
        user = User.objects.get(pk=request.data["user_id"])
        PhysicianUser.objects.create(
            user=user,
            physician=physician
        )

        return Response({'message': 'User added'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def remove(self, request, pk):
        """Delete request for a user to leave an physician"""

        physician = Physician.objects.get(pk=pk)
        user = User.objects.get(pk=request.data["user_id"])
        physician_user = PhysicianUser.objects.filter(
            user=user,
            physician=physician
        )
        physician_user.delete()
        return Response({'message': 'User removed'}, status=status.HTTP_204_NO_CONTENT)
