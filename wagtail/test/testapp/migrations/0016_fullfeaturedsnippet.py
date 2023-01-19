# Generated by Django 4.0.8 on 2023-01-19 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0083_workflowcontenttype"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tests", "0015_gallerypage_gallerypageimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="FullFeaturedSnippet",
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
                (
                    "live",
                    models.BooleanField(
                        default=True, editable=False, verbose_name="live"
                    ),
                ),
                (
                    "has_unpublished_changes",
                    models.BooleanField(
                        default=False,
                        editable=False,
                        verbose_name="has unpublished changes",
                    ),
                ),
                (
                    "first_published_at",
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        null=True,
                        verbose_name="first published at",
                    ),
                ),
                (
                    "last_published_at",
                    models.DateTimeField(
                        editable=False, null=True, verbose_name="last published at"
                    ),
                ),
                (
                    "go_live_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="go live date/time"
                    ),
                ),
                (
                    "expire_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="expiry date/time"
                    ),
                ),
                (
                    "expired",
                    models.BooleanField(
                        default=False, editable=False, verbose_name="expired"
                    ),
                ),
                (
                    "locked",
                    models.BooleanField(
                        default=False, editable=False, verbose_name="locked"
                    ),
                ),
                (
                    "locked_at",
                    models.DateTimeField(
                        editable=False, null=True, verbose_name="locked at"
                    ),
                ),
                ("text", models.TextField()),
                (
                    "latest_revision",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.revision",
                        verbose_name="latest revision",
                    ),
                ),
                (
                    "live_revision",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.revision",
                        verbose_name="live revision",
                    ),
                ),
                (
                    "locked_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="locked_%(class)ss",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="locked by",
                    ),
                ),
            ],
            options={
                "verbose_name": "full-featured snippet",
                "verbose_name_plural": "full-featured snippets",
            },
            bases=(wagtail.models.WorkflowMixin, models.Model),
        ),
    ]