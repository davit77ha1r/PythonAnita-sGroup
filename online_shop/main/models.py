from django.db import models
from django.core.validators import MinValueValidator



STATUS_CHOICE = (
    (0, "Old"),
    (1, "New"),
)

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
	item_image = models.ImageField(default="/media/no_image.jpg",  upload_to = 'media')
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	price = models.PositiveIntegerField(default=0)
	discount = models.PositiveIntegerField(default=0)
	color = models.CharField(max_length = 50, blank = True)
	status = models.IntegerField(choices=STATUS_CHOICE, default=1)
	ref_num = models.BigIntegerField(default = 1, validators = [MinValueValidator(0)])

	def __str__(self):
		return self.name