# Generated by Django 4.2.8 on 2023-12-26 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("moovie_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="director",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="director_set",
                to="moovie_app.director",
            ),
        ),
    ]
