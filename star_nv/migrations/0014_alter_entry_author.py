# Generated by Django 4.1.3 on 2022-11-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star_nv', '0013_dog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.ManyToManyField(blank=True, related_name='author_name', to='star_nv.author'),
        ),
    ]
