from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils import timezone 
from django.contrib.auth.models import User




# Create your models here.
#this Files models is for Publications of faculty
#Pillow package is required for rendering image
class Files(models.Model):
    filename = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='store/pdfs/')
    cover = models.ImageField(upload_to='store/covers/', null=True, blank=True)

    def __str__(self):
        return self.filename

#models for handling achievements and announcements

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
        
    title = models.CharField(max_length=250)
    #excerpt is like a short description of ur main content
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = RichTextUploadingField(blank=False)
    status = models.CharField(max_length=10, choices=options, default='draft')
    publish = models.DateTimeField(default=timezone.now)
    
    newmanager = NewManager()# custom manager
    objects = models.Manager()  
    def get_absolute_url(self):
        return reverse('work:post_single', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title