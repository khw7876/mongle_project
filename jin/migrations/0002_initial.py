# Generated by Django 4.0.6 on 2022-07-13 05:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("jin", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="userlettertargetuser",
            name="target_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="letterreviewlike",
            name="review_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="jin.letterreview"
            ),
        ),
        migrations.AddField(
            model_name="letterreviewlike",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="letterreview",
            name="letter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="jin.letter"
            ),
        ),
        migrations.AddField(
            model_name="letterreview",
            name="review_author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="letter",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="jin.worrycategory"
            ),
        ),
        migrations.AddField(
            model_name="letter",
            name="letter_author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
