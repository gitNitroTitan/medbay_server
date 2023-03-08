from django.db import models
from .users import User
from .records import Record



class RecordUser(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
