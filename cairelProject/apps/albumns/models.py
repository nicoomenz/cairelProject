from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=50)
    departure_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=50)
    lyric = models.TextField(null=True, blank=True)
    mp3_file = models.FileField(upload_to='songs/mp3', null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')