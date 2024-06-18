from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    
    def __str__(self):
        return self.name 

class PetrusProject(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title  
                                   
class PetrusSkill(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name