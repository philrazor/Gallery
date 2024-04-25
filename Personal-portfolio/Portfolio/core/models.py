from django.db import models

class Book(models.Model):
    book_id  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True , null=True)
    image = models.ImageField(upload_to='book_images')

    def __str__(self):
        return self.title
    


