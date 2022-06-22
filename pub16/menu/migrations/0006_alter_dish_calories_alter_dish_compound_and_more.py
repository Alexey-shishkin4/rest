# Generated by Django 4.0.5 on 2022-06-05 08:28

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='calories',
            field=models.CharField(blank=True, max_length=100, verbose_name='Каллорийность'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='compound',
            field=models.TextField(blank=True, max_length=250, verbose_name='Состав'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='upload',
            field=sorl.thumbnail.fields.ImageField(blank=True, default=None, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='weight',
            field=models.CharField(blank=True, max_length=100, verbose_name='Масса'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='item_image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]