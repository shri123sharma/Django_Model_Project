# Generated by Django 4.1.3 on 2022-11-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star_nv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=59, null=True)),
                ('shrit_size', models.CharField(blank=True, choices=[('Small', 'S'), ('Medium', 'M'), ('Large', 'L')], max_length=50, null=True)),
            ],
        ),
    ]
