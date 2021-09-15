from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.http import HttpResponseRedirect

User._meta.get_field('email')._unique = True

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to="profiles/", null=True)
	bio = models.TextField(null=True)

	def __str__(self):
		return self.user.username


class NoteBook(models.Model):

	COLOR_CHOICES = [
		('#ccf', 'Blue'),
		('red', 'DarkRed'),
		('#cfc', 'Green'),
		('#ffc', 'Yellow'),
		('CadetBlue', 'CadetBlue'),
		('Lavender', 'Lavender'),
		('#ffcce5', 'Pink'),
		('BurlyWood', 'BurlyWood'),
		('#f9f9f9','Silver'),
		('Cornsilk','Cornsilk'),
		('IndianRed ','IndianRed '),
		('LightGreen','LightGreen'),
		('LightSlateGray','LightSlateGray'),
		('PaleGoldenRod','PaleGoldenRod')
	]

	name = models.CharField(max_length=255)
	description = models.TextField()
	owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	is_public = models.BooleanField(default=False)
	color = models.CharField(choices=COLOR_CHOICES, default='Lavender', max_length=30)

	def __str__(self):
		return self.name + ' by ' + self.owner.user.username

	def get_absolute_url(self):
		return HttpResponseRedirect(reverse("detailed_notebook", kwargs={"id":self.id}))


class Note(models.Model):

	COLOR_CHOICES = [
		('#ccf', 'Blue'),
		('red', 'DarkRed'),
		('#cfc', 'Green'),
		('#ffc', 'Yellow'),
		('CadetBlue', 'CadetBlue'),
		('Lavender', 'Lavender'),
		('#ffcce5', 'Pink'),
		('BurlyWood', 'BurlyWood'),
		('#f9f9f9','Silver'),
		('Cornsilk','Cornsilk'),
		('IndianRed ','IndianRed '),
		('LightGreen','LightGreen'),
		('LightSlateGray','LightSlateGray'),
		('PaleGoldenRod','PaleGoldenRod')
	]

	title = models.CharField(max_length=255, null=False)
	content = models.TextField()
	color = models.CharField(choices=COLOR_CHOICES, default='yellow', max_length=30)
	created_at = models.DateTimeField(auto_now=True)
	notebook = models.ForeignKey(NoteBook, on_delete=models.CASCADE)

	def __str__(self):
		return self.title





def create_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = Profile.objects.get_or_create(user=instance)  

post_save.connect(create_profile, sender=User)