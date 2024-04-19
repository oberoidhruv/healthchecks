# Generated by Django 2.1.5 on 2019-01-12 14:27

from __future__ import annotations

from typing import Any

from django.apps.registry import Apps
from django.db import migrations


def fill_project_id(apps: Apps, schema_editor: Any) -> None:
    Project = apps.get_model("accounts", "Project")
    Check = apps.get_model("api", "Check")
    Channel = apps.get_model("api", "Channel")
    for project in Project.objects.all():
        Check.objects.filter(user_id=project.owner_id).update(project=project)
        Channel.objects.filter(user_id=project.owner_id).update(project=project)


class Migration(migrations.Migration):
    dependencies = [("api", "0054_auto_20190112_1427")]

    operations = [migrations.RunPython(fill_project_id, migrations.RunPython.noop)]