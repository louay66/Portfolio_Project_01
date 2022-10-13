from datetime import datetime

import uuid as uuid
from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import RegexValidator


class Category(models.Model):
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    new_category = models.CharField(max_length=15)

    def __str__(self):
        return self.new_category


class Guest(models.Model):
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=10, null=True)
    phone_number = models.CharField(max_length=8, null=True)
    delivery = models.DateField(verbose_name="date of delivery the prodact", null=True)
    receipt = models.DateField(verbose_name="date of receipt the prodact", null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def delivery_get(self):
        return self.delivery


class Prodact(models.Model):
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='%y/%m/%d')

    # @property
    # def delivery(self):
    #     return "{}".format()

    @property
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="300" weight="300"/>'.format(self.image.url))
        else:
            return ""

    def image_table(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="70" />'.format(self.image.url))
        else:
            return ""

    #     active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True)
    prodact = models.ForeignKey(Prodact, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.guest.__str__()


