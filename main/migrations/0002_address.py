# Generated by Django 2.2.13 on 2020-06-08 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("main", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=60)),
                (
                    "address1",
                    models.CharField(max_length=60, verbose_name="Address Line 1"),
                ),
                (
                    "address2",
                    models.CharField(
                        blank=True, max_length=60, verbose_name="Address Line 2"
                    ),
                ),
                (
                    "pin_code",
                    models.CharField(max_length=12, verbose_name="ZIP / Postal Code"),
                ),
                ("city", models.CharField(max_length=60)),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("in", "India"),
                            ("en", "England"),
                            ("us", "United States of America"),
                        ],
                        max_length=3,
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
            options={"abstract": False},
        )
    ]