from django.conf import settings
from django.db import models
from django.utils import timezone, dateformat
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.contrib.auth.models import User



# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    company = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    description = models.TextField(max_length=200)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.last_name)


User = get_user_model()

class email_photographer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    company = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    description = models.TextField(max_length=200)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.last_name)


class Customer(models.Model):
    #photographer_id = models.ForeignKey(Photographer, on_delete=models.CASCADE, related_name='Photographer')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer_id, self)


class Payment(models.Model):
    photographer_id = models.ForeignKey(Photographer, on_delete=models.CASCADE, related_name='Payment')
    payment_type = models.CharField(max_length=2)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    pin = models.CharField(max_length=4)
    p_description = models.TextField()

    def __str__(self):
        return str(self.customer_id)


class Photo(models.Model):
    photographer_id = models.ForeignKey(Photographer, on_delete=models.CASCADE, related_name='Photo')
    photo = models.CharField(max_length=60)
    uploaded_at = models.DateTimeField()

    def updated(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return str(self.event_id)


class Comment(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='Comment')
    photographer_id = models.ForeignKey(Photographer, on_delete=models.CASCADE, related_name='Comment')
    publish = models.CharField(max_length=2)
    photo = models.CharField(max_length=60)
    uploaded_at = models.DateTimeField()

    def updated(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return str(self.event_id)


class SocialLink(models.Model):
    photographer_id = models.ForeignKey(Photographer, on_delete=models.CASCADE, related_name='Link')
    site = models.CharField(max_length=50)
    link = models.CharField(max_length=250)

    def __str__(self):
        return str(self.photographer_id)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
