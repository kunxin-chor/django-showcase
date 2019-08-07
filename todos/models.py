from django.db import models

# Create your models here.

# declare a class named "Item"
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    ongoing = models.BooleanField(blank=False, default=False)
    completed_at = models.DateField(blank=True, null=True, default=None)
    category= models.ForeignKey("Category", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")
    
    def __str__(self):
        return self.name
        
        
class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.name
        
class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.name