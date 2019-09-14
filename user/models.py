from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from multiselectfield import MultiSelectField


CATEGORY_CHOICES = (('Shirts', 'Shirts'),
              ('Custiomised vest', 'Custiomised Vest'),
              ('Native wears', 'Native Wears'),
              ('Footwears', 'Footwears'),
              ('Trousers', 'Trousers'),
			  ('Caps', 'Caps'))
class UserProfile(models.Model):
							user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
							area = models.CharField(max_length=10)
							city = models.CharField(max_length=10)
							country = models.CharField(max_length=10)
							state = models.CharField(max_length=10)
							tagline = models.CharField(max_length=33)	
							phoneNumber = models.CharField(max_length=15)	
							companyName = models.CharField(max_length=24)
							profileImage = models.ImageField()
							category=MultiSelectField(choices=CATEGORY_CHOICES, blank=True, null=True)
							address= models.CharField(max_length=100)
							aboutMe=models.TextField()
							last_visit = models.DateTimeField(blank=True, null=True)
							def __str__(self):
								return str(self.user)
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

class Category(models.Model):
		name = models.CharField(max_length=15)
		def __str__(self):
			return self.name

class Design(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, related_name='design_category', on_delete=models.CASCADE)
	designImage=models.ImageField()
	timeuploaded=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.user)