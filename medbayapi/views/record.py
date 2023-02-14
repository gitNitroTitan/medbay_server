from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from medbayapi.models import Physician, Record, User
from rest_framework.decorators import action
from rest_framework import generics
from medbayapi.serializers import RecordSerializer
from django.shortcuts import get_object_or_404


class RecordView(ViewSet):
  """ Medbay Record view"""

  def retrieve(self, request, pk):
    """Handles GET requests for single comment
    Returns:
      Response -- JSON serialized comment
    """
    record = Record.objects.get(pk=pk)
    serializer = RecordSerializer(record)
    return Response(serializer.data)

  def list(self, request):
      """Handle GET requests to get all records for physician
      Returns:
          Response -- JSON serialized list of records
      """
      records = Record.objects.all()

      physician = request.query_params.get('physician', None)
      if physician is not None:
        records = records.filter(physician=physician)
      serializer = RecordSerializer(records, many=True)

      return Response(serializer.data)

  def create(self, request):
      """Handle POST operations

      Returns
          Response -- JSON serialized comment instance
      """
      user = User.objects.get(uid = request.data["user"])
      physician = Physician.objects.get(pk = request.data["physician"])

      record = Record.objects.create(
          name = request.data["name"],
          url = request.data["url"],
          latitude = request.data["latitude"],
          longitude = request.data["longitude"],
          description = request.data["description"],
          physician = physician,
          user = user
      )
      serializer = RecordSerializer(record)
      return Response(serializer.data)

  def update(self, request, pk):
    """Handle PUT requests for a comment

    Returns:
        Response -- Empty body with 204 status code
    """
    physician = Physician.objects.get(pk = request.data["physician"])

    record = Record.objects.get(pk=pk)
    record.description = request.data["description"]
    record.latitude = request.data["latitude"]
    record.longitude = request.data["longitude"]
    physician = Physician.objects.get(pk=request.data["physician"])
    record.physician = physician
    record.save()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

  def destroy(self, request, pk):
    record = Record.objects.get(pk=pk)
    record.delete()

    return Response(None, status=status.HTTP_204_NO_CONTENT)
