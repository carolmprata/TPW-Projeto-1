# Generated by Django 4.2.16 on 2024-11-09 01:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20241109_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='artist',
        ),
        migrations.AlterField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='app.product'),
        ),
        migrations.CreateModel(
            name='FavoriteArtist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritesArtist', to='app.artist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritesArtist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
