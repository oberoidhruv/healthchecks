# Generated by Django 3.2.6 on 2021-09-07 09:19

from __future__ import annotations

from typing import Any

from django.apps.registry import Apps
from django.db import migrations
from django.utils.text import slugify


def fill_slug(apps: Apps, schema_editor: Any) -> None:
    Check = apps.get_model("api", "Check")
    for c in Check.objects.exclude(name="").only("name"):
        Check.objects.filter(id=c.id).update(slug=slugify(c.name))


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0079_auto_20210907_0918"),
    ]

    operations = [migrations.RunPython(fill_slug, migrations.RunPython.noop)]
