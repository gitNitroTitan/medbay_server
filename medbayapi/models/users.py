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

    # @property
    # def hikes(self):
    #     """user hikes"""
    #     hikes = [hike for hike in self.user_hike.all()]
    #     return hikes

    # @property
    # def boards(self):
    #     """user hikes"""
    #     boards = [board for board in self.user_board.all()]
    #     return boards
