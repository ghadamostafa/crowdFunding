from django.db import models
from Users.models import Users
from django.utils import timezone


class Categories(models.Model):
	id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Projects(models.Model):
	Title=models.CharField(max_length=100)
	Details=models.TextField()
	target=models.IntegerField()
	start_date=models.DateField(auto_now=False, auto_now_add=False , default=timezone.now)
	end_date=models.DateField(auto_now=False, auto_now_add=False)
	report=models.IntegerField(null=True)
	user=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='UserID')
	category=models.ForeignKey('Categories', on_delete=models.CASCADE,null=True)
	tags = models.ManyToManyField('Tags', through='project_tags')
	donations=models.ManyToManyField(Users, through='user_donations',related_name='UserDonations')
	class Meta:
		db_table = "Projects"
	def __str__(self):
		return self.Title
	

class Pictures(models.Model):
	id=models.AutoField(primary_key=True)
	project = models.ForeignKey(Projects,on_delete=models.CASCADE,null=True)
	image=models.ImageField(upload_to='images/projects',verbose_name="image",null=True)
	user_id=models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
	# project_Id=models.ForeignKey(Projects, on_delete=models.CASCADE,null=True)
	
	class Meta:
		db_table = "Project_Pictures"


class Tags(models.Model):
	name=models.CharField(max_length=255,null=True)
	class Meta:
		db_table = "Tags"
	def __str__(self):
		return self.name


class Rates(models.Model):
	rate=models.DecimalField(max_digits=3,decimal_places=1)
	project=models.ForeignKey('Projects',on_delete=models.CASCADE)
	user=models.ForeignKey(Users,on_delete=models.CASCADE)
	class Meta:
		db_table = "Project_Rates"
	def __str__(self):
		return str(self.rate)+" on "+self.project.Title +" project"


class Comments(models.Model):
	body=models.TextField()
	report=models.IntegerField(null=True)
	project=models.ForeignKey('Projects',on_delete=models.CASCADE)
	user=models.ForeignKey(Users,on_delete=models.CASCADE)
	class Meta:
		db_table = "Project_Comments"
	def __str__(self):
		return self.body+" on "+self.project.Title


class project_tags(models.Model):
	tag=models.ForeignKey('Tags',on_delete=models.CASCADE)
	project=models.ForeignKey('Projects',on_delete=models.CASCADE)
	class Meta:
		unique_together =['tag','project']
		db_table = "project_tags"


class user_donations(models.Model):
	user=models.ForeignKey(Users,on_delete=models.CASCADE)
	project=models.ForeignKey('Projects',on_delete=models.CASCADE)
	Amount=models.IntegerField()
	class Meta:
		# index_together = ["user", "project"]
		unique_together =['user','project']
		db_table = "User_Donations"


class Featured_projects(models.Model):
	featured=models.BooleanField()
	featured_date=models.DateTimeField(default=timezone.now,auto_now=False, auto_now_add=False)
	project=models.ForeignKey('Projects',on_delete=models.CASCADE)
	def __str__(self):
		return self.project.Title

