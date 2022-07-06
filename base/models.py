
from email.policy import default
from re import T
from django.db import models
import uuid
from ckeditor_uploader.fields  import RichTextUploadingField
from django.utils.text import slugify
# Create your models here.




class tag(models.Model):
    name = models.CharField(max_length=200,null=True)    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name     

class Project(models.Model):
    title = models.CharField(max_length=200,null=True)
    sub_headline = models.CharField(max_length=200, blank=True, null=True, )
    thumbnail = models.ImageField(null=True ,upload_to="images", default="/images/placeholder.png")
    body = RichTextUploadingField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    tags = models.ManyToManyField(tag,null=True)
    SourceLink = models.CharField(max_length=500,null=True,blank=True)
    APILink = models.CharField(max_length=500,null=True,blank=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Project.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count) 
                has_slug = Project.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)



class Skill(models.Model):
    title = models.CharField(max_length=200,null=True)
    body = RichTextUploadingField(null=True, blank=True)
    sub_body = models.TextField( blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    icon = models.CharField(max_length=200,null=True, default="bx bx-code",blank=True)

    def __str__(self):
        return self.title       






class Home(models.Model):
    title = models.CharField(max_length=200,null=True)
    sub_title = models.CharField(max_length=200,null=True)
    description = models.TextField(blank=True, null=True)
   
    
   

    def __str__(self):
        return self.title       


class About(models.Model):
    description = models.TextField(blank=True, null=True) 
    Photo = models.ImageField(null=True ,upload_to="images", default="images/about.jpg")
    title1 = models.CharField(max_length=200,null=True,blank=True)
    description1 = models.CharField(max_length=200,null=True,blank=True)
    title2 = models.CharField(max_length=200,null=True,blank=True)
    description2 = models.CharField(max_length=200,null=True,blank=True)
    title3 = models.CharField(max_length=200,null=True,blank=True)
    description3 = models.CharField(max_length=200,null=True,blank=True)
    resume = models.CharField(max_length=500,null=True,blank=True) 
    
    
    
   

    def __str__(self):
        return self.title1  




     
