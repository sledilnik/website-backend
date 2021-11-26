# Generated by Django 3.1.7 on 2021-11-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0008_auto_20211125_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='slug',
            field=models.SlugField(blank=True, help_text='Used to reference the question with a hash link, e.g. https://sledilnik.org/faq#slug', max_length=100, null=True, verbose_name='Slug'),
        ),
    ]