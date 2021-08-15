from django.db import models
from django.urls import reverse

# Create your models here.

class Products(models.Model):

	name = models.CharField(max_length = 120)
	description = models.TextField(blank = True, null = True)
	price = models.DecimalField(decimal_places = 2, max_digits = 1000)
	summary = models.TextField()
	featured = models.BooleanField(null = True)

	def get_absolute_url(self):
    		return reverse("dynamic_details", kwargs={"my": self.id})
	
	
	