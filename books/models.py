from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):

	title = models.TextField(default='Book One')

	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

	# author = models.ManyToManyField(User, related_name='books')	


	content = models.TextField(default='Some text goes here')

	created_at = models.DateTimeField(auto_now_add=True)

	updated_at = models.DateTimeField(auto_now=True)

	editable = models.BooleanField(default=True)

	goal = models.IntegerField(default=1000)

	is_finished = models.BooleanField(default=False)

	wordsPerPeriod = models.IntegerField(default=500)

	timePeriod = models.IntegerField(default=30)

	out_of_time = models.BooleanField(default=False)

	time_total = models.IntegerField(default=10000)

	def __str__(self):
   		return 'Book: ' + self.title

	class Meta:
		get_latest_by = "created_at"



class Library(models.Model):

	name = models.TextField(default="New Library")

	books = models.ManyToManyField(Book, related_name="libraries")


	def __str__(self):
   		return 'Library: ' + self.name



