from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    screenshot = models.ImageField(upload_to='screenshots/', blank=True, null=True)

    def __str__(self):
        return self.title
