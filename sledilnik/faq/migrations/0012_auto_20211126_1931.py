# Generated by Django 3.1.7 on 2021-11-26 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0011_auto_20211126_1921'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='faq',
            name='unique_question_per_project',
        ),
        migrations.RemoveConstraint(
            model_name='glossaryterm',
            name='unique_slug_sl_per_project',
        ),
        migrations.RemoveConstraint(
            model_name='glossaryterm',
            name='unique_slug_en_per_project',
        ),
        migrations.AlterField(
            model_name='faq',
            name='slug',
            field=models.SlugField(default='', help_text='Used to reference the question with a hash link, e.g. https://sledilnik.org/faq#slug', max_length=100, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faq',
            name='slug_en',
            field=models.SlugField(help_text='Used to reference the question with a hash link, e.g. https://sledilnik.org/faq#slug', max_length=100, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='slug_sl',
            field=models.SlugField(help_text='Used to reference the question with a hash link, e.g. https://sledilnik.org/faq#slug', max_length=100, null=True, verbose_name='Slug'),
        ),
        migrations.AddConstraint(
            model_name='faq',
            constraint=models.UniqueConstraint(fields=('project', 'slug'), name='unique_faq_slug_per_project'),
        ),
        migrations.AddConstraint(
            model_name='faq',
            constraint=models.UniqueConstraint(fields=('project', 'question'), name='unique_faq_question_per_project'),
        ),
        migrations.AddConstraint(
            model_name='glossaryterm',
            constraint=models.UniqueConstraint(fields=('project', 'slug_sl'), name='unique_glossary_slug_per_project'),
        ),
        migrations.AddConstraint(
            model_name='glossaryterm',
            constraint=models.UniqueConstraint(fields=('project', 'term'), name='unique_glossary_term_per_project'),
        ),
    ]
