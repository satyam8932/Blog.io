from django.db import models
from django.utils.html import format_html

# Create your models here.

# creating categories of the blog
class Category(models.Model):
    ID = models.AutoField(primary_key=True)   #No. of blogs automatically increases using primary keys
    Title = models.CharField(max_length=100)
    Description = models.TextField(null=True)
    url = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='category/')
    Date = models.DateTimeField(auto_now_add=True, null=True)

    # Methods to show image in Category for admin dashboard
    def imageTag(self):
        return format_html(f'<img src="/media/{self.Image}" style="width:80px;height:50px"     />')
    
    # Methods to show th title in the filter 
    def __str__(self):
        return self.Title
    
    
    
# creating posts of the blogs
class Posts(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    url = models.CharField(max_length=100)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='post/')
    
    # Methods to show image in Category for admin dashboard
    def imageTag(self):
        return format_html(f'<img src="/media/{self.Image}" style="width:80px;height:50px"     />')
    
    # Methods to show th title in the filter 
    def __str__(self):
        return self.Title
    
    