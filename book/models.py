from django.db import models
from django.utils import timezone

class Book(models.Model):
	title = models.CharField(max_length=100)
	writer = models.CharField(max_length=100, default='unknown author')
	summary = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	GENRES = (
		('SF', 'Science Fiction'),
		('F', 'Fantasy'),
		('Myt', 'Mythology'),
		('Ad', 'Adventure'),
		('Mys', 'Mystery'),
		('Dr', 'Drama'),
		('Rom', 'Romance'),
		('Hor', 'Horror'),
		('Com', 'Comdey'),
		('Th', 'Thriller'),
		('Dy', 'Dystopia'),
	)
	genre = models.CharField(max_length=3, choices=GENRES, default='SF')

	def __str__(self):
		return self.title