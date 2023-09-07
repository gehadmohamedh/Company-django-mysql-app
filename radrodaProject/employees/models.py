from django.db import models
from django.urls import reverse
from departments.models import department

# Create your models here.
class employee (models.Model):
    
    name = models.CharField(max_length=10)
    email = models.EmailField(null=True, max_length=254, blank=True)
    age = models.IntegerField(default=15)
    img = models.ImageField(upload_to="students", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True , null=True)
    created_at = models.DateField(auto_now_add=True , null=True)
    dept = models.ForeignKey(department, null=True , blank=True ,
                             on_delete = models.CASCADE , 
                             related_name="same_dep_coll")
    
    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def get_all_emps(cls):
        return cls.objects.all()
    
    @classmethod
    def get_emp (cls , id ):
        return cls.objects.get(id = id)
    
    def get_delete_url(self):
        print (reverse("employees.delete", args=[self.id]))
        return reverse("employees.delete", args=[self.id])
    
    def get_display_url(self):
        return reverse("employees.display", args=[self.id]) 
    
    def get_image_url(self):
        print ("/media/{self.img}")
        return f"/media/{self.img}"
    
    def get_edit_url(self):
        return reverse("employees.edit", args=[self.id])