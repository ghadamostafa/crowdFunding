from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone=models.CharField( max_length=11)
	Img=models.ImageField(upload_to='images/Users', null=True, blank=True)
	BirthDate=models.DateField(auto_now=False, auto_now_add=False,null=True)
	faceBook=models.URLField(null=True)
	country=models.CharField(max_length=100,null=True)
	class Meta:
		db_table = "Profile"
	def __str__(self):
		return self.first_name

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# class User_optional_Info(models.Model):
	
# 	user=models.ForeignKey(User,on_delete=models.CASCADE)
# 	class Meta:
# 		db_table = "User_optional_Info"

