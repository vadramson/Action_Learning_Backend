from django.db import models
from django.utils import timezone


# Create your models here.
class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name


class Clothings(models.Model):
    file = models.FileField(blank=False, null=False)
    status = models.BooleanField(verbose_name='Status', default=False)
    price = models.FloatField(verbose_name='price', null=False, blank=False, default=1.0)
    category = models.CharField(max_length=255, null=False, blank=False, verbose_name='Category', default="inter")
    clothing_description = models.TextField(null=False, blank=False, verbose_name='clothing_description')
    dateRegistered = models.DateTimeField(default=timezone.now)


class Predictions(models.Model):
    predicted = models.CharField(max_length=255, null=False, blank=False, verbose_name='predicted')
    image_id = models.IntegerField(null=False, blank=False, verbose_name='predicted_image')
    accuracy_of_prediction = models.FloatField(verbose_name='accuracy_of_prediction', null=False, blank=False, default=0.0)
    true_predict = models.IntegerField(null=False, blank=False, default=2, verbose_name='Was_prediction_true')
    corrected_prediction = models.CharField(max_length=255, null=False, blank=False, verbose_name='corrected_prediction')
    dateRegistered = models.DateTimeField(default=timezone.now)

