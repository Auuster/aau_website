from django.db import models
from django.utils import timezone
from users.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
	title = models.CharField(max_length=100)
	writer = models.CharField(max_length=100, default='unknown author')
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

class Review(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	date_posted = models.DateField(default=timezone.now)
	review = models.TextField()
	reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE)
	rating = models.IntegerField(default=8, validators=[MaxValueValidator(8), MinValueValidator(0)])

	def __str__(self):
		return f'{self.book.title} by {self.reviewer.user.username}'
