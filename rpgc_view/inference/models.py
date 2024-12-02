# Inference Models
# BoMeyering 2024

import uuid
import os
from django.db import models
from django.db import transaction
from PIL import Image
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from guardian.shortcuts import assign_perm

# from .file_storage import CustomFileStorage, TemporaryFileStorage
# Create your models here.

# final_storage = CustomFileStorage()
# temp_storage = TemporaryFileStorage()

# class ImageUpload(models.Model):
    # """_summary_

    # Args:
    #     models (_type_): _description_
    # """
    # uploadDbId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # imageName = models.CharField(max_length=80, null=True, blank=True)
    # imageSize = models.IntegerField(null=True, blank=True)
    # imageHeight = models.IntegerField(null=True, blank=True)
    # imageWidth = models.IntegerField(null=True, blank=True)
    # uploadTime = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='images/', storage=temp_storage)

    # def save(self, *args, **kwargs):
    #     if not self.uploadDbId:
    #         self.uploadDbId = uuid.uuid4()
    #     with transaction.atomic():
    #         try:
    #             super().save(*args, **kwargs)
    #             img = Image.open(self.image.path)
    #             print(self.image.path)
    #             self.imageName = self.image.name
    #             self.imageSize = self.image.size
    #             self.imageWidth = img.width
    #             self.imageHeight = img.height

    #             final_path = final_storage.save(self.image.name, self.image)
    #             print(final_path)
    #             os.rename(self.image.path, final_storage.path(final_path))
    #             self.image = final_path

    #             super().save(update_fields=['imageName', 'imageSize', 'imageWidth', 'imageHeight', 'image'])
    #             # super().save(update_fields=['imageName', 'image'])

    #         except Exception as e:
    #             if os.path.exists(self.image.path):
    #                 os.remove(self.image.path)
    #             raise e

# class ImageMetadata(models.Model):
#     imageDbId = models.UUIDField(default=uuid.uuid4)
#     imageTestField = models.CharField()

class Project(models.Model):
    projectDbId = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("project:project_detail", args=[self.slug])



class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    imageHeight = models.PositiveIntegerField()
    imageWidth = models.PositiveIntegerField()
    image = models.ImageField(null=True, blank=True, height_field=imageHeight, width_field=imageWidth)
    