# Generated by Django 3.1.7 on 2021-11-25 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0006_auto_20211125_1515'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Glossary',
            new_name='GlossaryTerm',
        ),
        migrations.AlterModelOptions(
            name='glossaryterm',
            options={'ordering': ['position'], 'verbose_name': 'Glossary term', 'verbose_name_plural': 'Glossary terms'},
        ),
    ]
