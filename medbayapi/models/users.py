from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    bio = models.CharField(max_length=1000)
    image_url = models.URLField(max_length=200)
    email = models.EmailField(max_length=256)
    location=models.CharField(max_length=1000)
    local_pharmacy=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    @property
    def physicians(self):
        """user physicians"""
        physicians = [physician for physician in self.user_physician.all()]
        return [physicians]

    @property
    def records(self):
        """user records"""
        records = [record for record in self.user_record.all()]
        return [records]
