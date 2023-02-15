from django.db import models
from .users import User
from .physicians import Physician



class PhysicianUser(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE)
