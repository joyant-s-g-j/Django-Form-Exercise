from django.db import models

# Create your models here.
class DummyModel(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
    