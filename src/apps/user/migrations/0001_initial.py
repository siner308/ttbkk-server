# Generated by Django 3.2.2 on 2021-05-09 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=50)),
                ('social_id', models.CharField(max_length=50)),
                ('social_type', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]