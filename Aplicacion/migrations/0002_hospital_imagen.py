# Generated by Django 2.0.1 on 2018-04-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]