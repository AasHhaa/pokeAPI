# Generated by Django 3.1.5 on 2021-02-02 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('corn', '0003_auto_20210129_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='owner',
        ),
        migrations.CreateModel(
            name='UserPokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corn.profile')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
