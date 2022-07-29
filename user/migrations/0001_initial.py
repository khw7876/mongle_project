# Generated by Django 4.0.6 on 2022-07-22 11:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main_page", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "username",
                    models.CharField(max_length=50, unique=True, verbose_name="사용자 계정"),
                ),
                ("password", models.CharField(max_length=128, verbose_name="비밀번호")),
                ("nickname", models.CharField(max_length=20, verbose_name="닉네임")),
                (
                    "create_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="가입일"),
                ),
                (
                    "update_date",
                    models.DateTimeField(auto_now=True, verbose_name="갱신일"),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(default="")),
                ("mongle_level", models.IntegerField(default=0)),
                ("mongle_grade", models.IntegerField(default=0)),
                ("fullname", models.TextField(default="")),
                (
                    "profile_img",
                    models.URLField(
                        default="https://user-images.githubusercontent.com/55477835/178631292-f381c6e2-2541-4a2c-ba67-b5bb4369e3d0.jpeg"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfileCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main_page.worrycategory",
                    ),
                ),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.userprofile",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="userprofile",
            name="categories",
            field=models.ManyToManyField(through="user.UserProfileCategory", to="main_page.worrycategory"),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="user",
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name="ReportedUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("report_reason", models.CharField(max_length=150)),
                (
                    "report_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "reported_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.reporteduser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MongleGrade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("grade", models.IntegerField(default=0)),
                (
                    "mongle",
                    models.URLField(
                        default="https://user-images.githubusercontent.com/55477835/178631292-f381c6e2-2541-4a2c-ba67-b5bb4369e3d0.jpeg"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
