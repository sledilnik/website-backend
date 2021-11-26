# Generated by Django 3.1.7 on 2021-11-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0012_auto_20211126_1931'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='glossaryterm',
            name='unique_glossary_slug_per_project',
        ),
        migrations.AddConstraint(
            model_name='glossaryterm',
            constraint=models.UniqueConstraint(fields=('project', 'slug'), name='unique_glossary_slug_per_project'),
        ),
    ]