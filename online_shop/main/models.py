from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import CharField, Model
from django_mysql.models import ListCharField


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
	list_1 = ['product']
	name = models.CharField(max_length = 150)
	brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
	tags = models.TextField(blank = True)
	description = models.TextField(blank = True)
	item_image = models.ImageField(default="/media/no_image.jpg",  upload_to = 'media')
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	price = models.PositiveIntegerField(default=0)
	discount = models.PositiveIntegerField(default=0)
	color = models.CharField(max_length = 50, blank = True)
	status = models.IntegerField(choices=STATUS_CHOICE, default=1)
	ref_num = models.TextField(unique=True)
	def disc(self):
		answer = round(self.price*(1-self.discount/100), 2)
		return answer

	def __str__(self):
		return self.name

