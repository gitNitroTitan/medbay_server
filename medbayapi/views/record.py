from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from medbayapi.models import Record, User
from medbayapi.serializers import RecordSerializer
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

        user = request.query_params.get('user', None)
        if user is not None:
            records = records.filter(user_id=user)
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized comment instance
        """
        user = User.objects.get(pk=request.data["user"])

        record = Record.objects.create(
            name=request.data["name"],
            dosage=request.data["dosage"],
            treatment=request.data["treatment"],
            date_prescribed=request.data["date_prescribed"],
            user=user
        )
        serializer = RecordSerializer(record)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a comment

        Returns:
            Response -- Empty body with 204 status code
        """
        # physician = Physician.objects.get(pk=request.data["physician_id"])

        record = Record.objects.get(pk=pk)
        record.name = request.data["name"]
        record.dosage = request.data["dosage"]
        record.treatment = request.data["treatment"]
        record.date_prescribed = request.data["date_prescribed"]
        # physician = Physician.objects.get(pk=request.data["physician"])
        # record.physician = physician
        record.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        record = Record.objects.get(pk=pk)
        record.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class RecordUserView(generics.ListCreateAPIView):
    serializer_class = RecordSerializer
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Record.objects.filter(user__id=user_id)
