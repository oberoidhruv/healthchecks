# Generated by Django 3.0.7 on 2020-07-01 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0071_check_manual_resume"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="owner",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="api.Check"
            ),
        ),
    ]