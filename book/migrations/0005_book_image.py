# Generated by Django 2.1.5 on 2019-01-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default_book.png', upload_to='books'),
        ),
    ]
