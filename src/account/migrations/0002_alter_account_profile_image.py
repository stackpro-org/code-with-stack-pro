# Generated by Django 3.2.4 on 2022-10-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_images/d.png', max_length=255, null=True, upload_to=''),
        ),
    ]
