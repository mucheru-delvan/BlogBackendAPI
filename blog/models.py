from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, 
        blank=True, 
        related_name='posts'
        )
    
    tags = models.ManyToManyField(
        Tag, 
        related_name='posts'
        )
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
