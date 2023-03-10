# Generated by Django 4.1.4 on 2023-02-07 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_rating_remove_movie_name_movie_movie_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='relase_year',
            new_name='release_year',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='description',
        ),
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='movies_app.movie'),
            preserve_default=False,
        ),
    ]
