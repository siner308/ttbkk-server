# Generated by Django 3.2.2 on 2021-07-27 14:25

from django.db import migrations, models
import django.db.models.deletion

from django.db import migrations


def forwards(apps, schema_editor):
    Place = apps.get_model('place', 'Place')
    places = Place.objects.all()
    print(len(places))
    for place in places:
        print(place.latitude, place.longitude)
        place.latitude = round(place.latitude, 10)
        place.longitude = round(place.longitude, 10)
        place.save()
        print(place.latitude, place.longitude)


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_id'),
        ('place', '0005_alter_place_is_deleted'),
    ]

    operations = [
        migrations.RunPython(forwards),
        migrations.AlterField(
            model_name='place',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_places', related_query_name='create_place', to='user.user'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='place',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_places', related_query_name='update_place', to='user.user'),
        ),
    ]