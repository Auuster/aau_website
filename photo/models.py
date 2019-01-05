from django.db import models
from django.utils import timezone
from PIL import Image

class Picture(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	image = models.ImageField(default='default.png', upload_to='pictures')
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		output_size = (800, 400)
		img.thumbnail(output_size, Image.ANTIALIAS)
		img.save(self.image.path)