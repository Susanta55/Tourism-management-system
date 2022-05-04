from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class about(models.Model):
    about_text = RichTextField()


class term(models.Model):
    terms_text = RichTextField()
