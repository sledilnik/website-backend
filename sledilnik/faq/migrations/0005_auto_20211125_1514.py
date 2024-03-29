# Generated by Django 3.1.7 on 2021-11-25 14:14

from django.db import migrations, models
import django.db.models.deletion
import sledilnik.easymde.models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0004_auto_20211124_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='Position')),
                ('slug', models.SlugField(help_text='Used to reference the term in the text: <span data-term="slug">some term</span>', max_length=100, verbose_name='Slug')),
                ('term', models.CharField(max_length=100, verbose_name='Term')),
                ('definition', sledilnik.easymde.models.MarkdownField(verbose_name='Definition')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.AddConstraint(
            model_name='faq',
            constraint=models.UniqueConstraint(fields=('project', 'question'), name='unique_question_per_project'),
        ),
        migrations.AddField(
            model_name='glossary',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glossary', to='faq.project', verbose_name='Project'),
        ),
        migrations.AddConstraint(
            model_name='glossary',
            constraint=models.UniqueConstraint(fields=('project', 'slug'), name='unique_slug_per_project'),
        ),
    ]
