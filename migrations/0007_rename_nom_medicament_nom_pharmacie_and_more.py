# Generated by Django 4.2.1 on 2023-11-02 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MedecineApp", "0006_remove_medicament_id_pharmacie_alter_medicament_nom"),
    ]

    operations = [
        migrations.RenameField(
            model_name="medicament",
            old_name="nom",
            new_name="nom_pharmacie",
        ),
        migrations.RenameField(
            model_name="pharmacie",
            old_name="nom",
            new_name="nom_pharmacie",
        ),
        migrations.AddField(
            model_name="medicament",
            name="nom_medicament",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
