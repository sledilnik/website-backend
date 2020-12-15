# Generated by Django 3.1.4 on 2020-12-15 09:14

from django.db import migrations, models
import sledilnik.easymde.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restriction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_sl', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('rule', sledilnik.easymde.models.MarkdownField(verbose_name='Rule')),
                ('rule_sl', sledilnik.easymde.models.MarkdownField(null=True, verbose_name='Rule')),
                ('rule_en', sledilnik.easymde.models.MarkdownField(null=True, verbose_name='Rule')),
                ('regions', models.CharField(max_length=255, verbose_name='Regions')),
                ('regions_sl', models.CharField(max_length=255, null=True, verbose_name='Regions')),
                ('regions_en', models.CharField(max_length=255, null=True, verbose_name='Regions')),
                ('exceptions', sledilnik.easymde.models.MarkdownField(blank=True, verbose_name='Rule exceptions')),
                ('exceptions_sl', sledilnik.easymde.models.MarkdownField(blank=True, null=True, verbose_name='Rule exceptions')),
                ('exceptions_en', sledilnik.easymde.models.MarkdownField(blank=True, null=True, verbose_name='Rule exceptions')),
                ('extra_rules', sledilnik.easymde.models.MarkdownField(blank=True, verbose_name='Extra rules')),
                ('extra_rules_sl', sledilnik.easymde.models.MarkdownField(blank=True, null=True, verbose_name='Extra rules')),
                ('extra_rules_en', sledilnik.easymde.models.MarkdownField(blank=True, null=True, verbose_name='Extra rules')),
                ('valid_since', models.DateField(blank=True, null=True, verbose_name='Valid since')),
                ('valid_until', models.DateField(blank=True, null=True, verbose_name='Valid until')),
                ('validity_comment', sledilnik.easymde.models.MarkdownField(blank=True, verbose_name='Validity comment')),
                ('validity_comment_sl', sledilnik.easymde.models.MarkdownField(blank=True, null=True, verbose_name='Validity comment')),
                ('validity_comment_en', sledilnik.easymde.models.MarkdownField(blank=True, null=True, verbose_name='Validity comment')),
                ('comments', sledilnik.easymde.models.MarkdownField(blank=True, verbose_name='Comments')),
                ('comments_sl', sledilnik.easymde.models.MarkdownField(blank=True, null=True, verbose_name='Comments')),
                ('comments_en', sledilnik.easymde.models.MarkdownField(blank=True, null=True, verbose_name='Comments')),
                ('legal_link', models.URLField(blank=True, null=True, verbose_name='Legal link')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]