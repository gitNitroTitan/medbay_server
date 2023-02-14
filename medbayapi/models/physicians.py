from django.db import models
from .users import User

class Physician(models.Model):
    """d"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name
