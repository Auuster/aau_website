# Generated by Django 2.1.5 on 2019-01-04 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.ImageField(default='default.png', upload_to='pictures'),
        ),
    ]
