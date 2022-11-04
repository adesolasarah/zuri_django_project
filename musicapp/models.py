from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name +  " " + self.last_name

class Song(models.Model):
    title = models.CharField(max_length=120)
    date_released = models.DateField(max_length=120)
    likes = models.IntegerField()
    artiste_id= models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        if self.date_released:
            return f"{self.title} ({self.date_released})"
        return self.title

class Lyric(models.Model):
    content = models.CharField(max_length=120)
    song_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

  