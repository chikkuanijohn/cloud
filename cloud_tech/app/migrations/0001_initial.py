# Generated by Django 5.1.2 on 2024-12-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('img', models.FileField(upload_to='course_images/')),
            ],
        ),
    ]
