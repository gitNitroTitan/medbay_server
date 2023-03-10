from django.db import models
from .users import User
# from .physicians import Physician

class Record(models.Model):
    """docstring
    """

    name = models.CharField(max_length=50)
    dosage = models.CharField(max_length=200)
    treatment = models.CharField(max_length=200)
    date_prescribed = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()


    def __str__(self):
        return self.name
