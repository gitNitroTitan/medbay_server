from rest_framework.serializers import ModelSerializer
from medbayapi.models import Record, Physician, User


class RecordSerializer(ModelSerializer):
    """JSON serializer for records
    """
    class Meta:
        model = Record
        fields = ('id', 'user', 'physician', 'name',
                  'dosage', 'treatment', 'date_prescribed')
        depth = 2

class PhysicianSerializer(ModelSerializer):
    """JSON serializer for physician
    """
    class Meta:
        model = Physician
        fields = ('id', 'user', 'name', 'specialty', 'email',
                'image_url', 'location', 'phone_number')
        depth = 2

class UserSerializer(ModelSerializer):
    """"JSON serializer for users"""
    # physician= PhysicianSerializer(many=True)
    # record= RecordSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'uid', 'name', 'age', 'bio', 'image_url',
                  'email', 'location', 'local_pharmacy')
