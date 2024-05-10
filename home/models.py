from django.db import models

# Create your models here.
class Band(models.Model):
    number = models.IntegerField(primary_key = True, editable = False)
    band_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.band_name

