# Generated by Django 5.1.4 on 2024-12-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course1", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chaivariety",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
