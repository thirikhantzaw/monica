from django.db import models
from ckeditor.fields import RichTextField
import uuid

# Create your models here.

class IntroModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = RichTextField()
    title = RichTextField()
    image = models.ImageField(upload_to='Intro/', null=True, blank=True)

    def __str__(self):
        return self.tag
    

class AboutModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = RichTextField(null=True, blank=True)
    title = RichTextField(null=True, blank=True)
    dec = RichTextField()

    def __str__(self):
        return self.tag



class ExpertiseOneModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = RichTextField(null=True, blank=True)
    title = RichTextField(null=True, blank=True)
    dec = RichTextField()

    def __str__(self):
        return self.tag


class ExpertiseTwoModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = RichTextField(null=True, blank=True)
    title = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.tag
    

class ClientModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = RichTextField(null=True, blank=True)
    title = RichTextField(null=True, blank=True)
    dec = RichTextField()

    def __str__(self):
        return self.tag
    

class LogoModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='Logo/', null=True, blank=True)

    def __str__(self):
        return self.tag
    

class TestimonialsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = RichTextField(null=True, blank=True)
    title = RichTextField(null=True, blank=True)
    dec = RichTextField()
    image = models.ImageField(upload_to='Testimonials/', null=True, blank=True)

    def __str__(self):
        return self.tag
    

class ContactModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = RichTextField(null=True, blank=True)
    title = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.tag
    


class JournalOneModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = RichTextField(null=True, blank=True)
    title = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.tag
    

class JournalTwoModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = RichTextField(null=True, blank=True)
    title = RichTextField(null=True, blank=True)
    dec = RichTextField()

    def __str__(self):
        return self.tag