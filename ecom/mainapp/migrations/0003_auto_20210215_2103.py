# Generated by Django 3.1.6 on 2021-02-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210215_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/', verbose_name='Product image'),
        ),
        migrations.AlterField(
            model_name='susi',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/', verbose_name='Product image'),
        ),
    ]
