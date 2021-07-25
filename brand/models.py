import uuid

from django.db import models

# Create your models here.
from hashtag.models import Hashtag
from user.models import User


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='create_brands',
                                   related_query_name='create_brand')
    updated_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='update_brands',
                                   related_query_name='update_brand')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
