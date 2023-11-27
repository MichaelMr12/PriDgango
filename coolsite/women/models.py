from django.db import models
#https://docs.djangoproject.com/en/4.2/ref/models/fields/
# Create your models here.
data_db = [{'id': 1, 'title': 'Илон Маск', 'content': 'Биография Маска', 'is_public': True},
           {'id': 2, 'title': 'Жириновский', 'content': 'Биография Жириновского', 'is_public': True},
           {'id': 3, 'title': 'Баба яга', 'content': 'Биография бабы яги', 'is_public': False},

           ]
class Students(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)