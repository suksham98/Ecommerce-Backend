# Generated by Django 5.0 on 2023-12-21 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]