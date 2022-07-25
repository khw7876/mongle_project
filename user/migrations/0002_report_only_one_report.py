# Generated by Django 4.0.6 on 2022-07-24 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="report",
            constraint=models.UniqueConstraint(
                fields=("report_user", "reported_user"), name="only_one_report"
            ),
        ),
    ]
