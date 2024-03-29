# Generated by Django 4.2.3 on 2023-09-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='logo',
            field=models.ImageField(default='default_logo.png', upload_to='business_logos/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='default_profile.png', upload_to='profile_images/'),
        ),
    ]
