from django.db import models

# Create your models here.
class LnadingPageEntry(models.Model):
    
    name= models.CharField(max_length=100 )
    email=models.EmailField()

    def __str__(self):
        return f"{self.email}"

    
