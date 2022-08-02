# Generated by Django 4.0.6 on 2022-07-30 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("worry_board", "0002_alter_worryboard_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="RequestStatus",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="worryboard",
            name="request_status",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="worry_board.requeststatus"
            ),
        ),
    ]
