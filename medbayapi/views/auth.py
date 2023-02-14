from rest_framework.response import Response
from rest_framework.decorators import api_view
from medbayapi.serializers import UserSerializer
from medbayapi.models import User



@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User

    Method arguments:
      request -- The full HTTP request object
    '''

    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    try:
        user = User.objects.get(uid=uid)

        serializers = UserSerializer(user)
        return Response(serializers.data)

    except:
        data = { 'valid':False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the medbayapi_user table
    user = User.objects.create(
        uid=request.data['uid'],
        name=request.data['name'],
        age=request.data['age'],
        bio=request.data['bio'],
        image_url=request.data['imageUrl'],
        email=request.data['email'],
        location=request.data['location'],
        local_pharmacy=request.data['localPharmacy'],
    )

    # Return the user info to the client
    data = {
            'id': user.id,
            'uid': user.uid,
            'name': user.name,
            'age': user.age,
            'bio': user.bio,
            'image_url': user.image_url,
            'email': user.email,
            'location': user.location,
            'local_pharmacy': user.local_pharmacy,
    }
    return Response(data)
