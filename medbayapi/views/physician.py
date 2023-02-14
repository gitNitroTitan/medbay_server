from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from medbayapi.models import Physician, Record, User
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
        user = User.objects.get(pk=request.data["user"])

        physician = Physician.objects.create(
                name=request.data["name"],
                specialty=request.data["specialty"],
                email=request.data["email"],
                location=request.data["location"],
                phone_number=request.data["phone_number"],
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
        physician.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        physician = Physician.objects.get(pk=pk)
        physician.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
