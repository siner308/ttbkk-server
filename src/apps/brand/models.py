import uuid

from django.db import models

# Create your models here.
from src.apps.hashtag.models import Hashtag
from src.apps.user.models import User


class Brand(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=uuid.uuid4)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True, db_table='brand_hashtags')
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='create_brands',
                                   related_query_name='create_brand')
    updated_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='update_brands',
                                   related_query_name='update_brand')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brand'
