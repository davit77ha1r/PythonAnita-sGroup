from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
	name = models.TextField()

	def __str__(self):
		return self.name
class Brand(models.Model):
	name = models.CharField(max_length = 60)

	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length = 150)
	brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
	description = models.TextField(blank = True)
	item_image = models.ImageField(default = "no_image.png",  upload_to = 'media')
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	price = models.PositiveIntegerField()
	color = models.CharField(max_length = 50, blank = True)
	ref_num = models.BigIntegerField(default = 1, validators = [MinValueValidator(0)])

	def __str__(self):
		return self.name