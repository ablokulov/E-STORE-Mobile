from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STAFF = "STAFF", "Staff"
        USER  = "USER", "User"
        
    email = models.EmailField(max_length=254,unique=True)
    role  = models.CharField(max_length=7,default=Role.USER,choices=Role.choices)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"username: {self.username} | email: {self.email}"   
    
    
    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    @property
    def is_user(self):
        return self.role == self.Role.USER


class Profile(models.Model):
    user = models.OneToOneField(
        User,on_delete=models.CASCADE,related_name="profile"
    )
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    phone      = models.CharField(max_length=15,blank=True)
    
    
    def __str__(self):
        return f"Profile: {self.user}"
    
    
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=50)
    
    is_default = models.BooleanField(default=False)   
    
    
    def __str__(self):
        return self.city