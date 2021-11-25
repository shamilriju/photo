# Generated by Django 3.2.8 on 2021-11-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='image',
            field=models.ImageField(default=2, upload_to='photos'),
            preserve_default=False,
        ),
    ]