from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# The idea I have going is that I will build a gallery for the miniatures I have painted.

class Post(models.Model):

    # Post Status field, Let's start with the basics. 
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # Setting up fields for posts
    # TODO Add a field for image upload 
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()

    # This block of code was giving me trouble, so I decided to remove it for now considering I will be the only person uploading to the gallery. 
    # author = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name='gallery_upload'
    # )

    # Published dates for posts. I'm not sure if this will be necessary in the end. I haven't quite figure out how the final layout will be.  
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    # Establishing a default sort order. 

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    def __str__(self):
        return self.title

