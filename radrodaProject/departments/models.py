from django.db import models
from django.urls import reverse

# Create your models here.
class department (models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100 , null = True , blank=True)
    updated_at = models.DateTimeField(auto_now=True , null=True)
    created_at = models.DateField(auto_now_add=True , null=True)
# Create your models here.
    
    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def get_all_deps(cls):
        return cls.objects.all()
    
    @classmethod
    def get_dep (cls , id ):
        return cls.objects.get(id = id)
    
    def get_display_url(self):
        return reverse("departments.display", args=[self.id]) 