# Generated by Django 3.1.7 on 2021-11-25 14:15

from django.db import migrations, models
import sledilnik.easymde.models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0005_auto_20211125_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='glossary',
            name='definition_en',
            field=sledilnik.easymde.models.MarkdownField(null=True, verbose_name='Definition'),
        ),
        migrations.AddField(
            model_name='glossary',
            name='definition_sl',
            field=sledilnik.easymde.models.MarkdownField(null=True, verbose_name='Definition'),
        ),
        migrations.AddField(
            model_name='glossary',
            name='term_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Term'),
        ),
        migrations.AddField(
            model_name='glossary',
            name='term_sl',
            field=models.CharField(max_length=100, null=True, verbose_name='Term'),
        ),
    ]
