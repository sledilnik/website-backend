# Generated by Django 3.1.4 on 2020-12-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='Author')),
                ('author_sl', models.CharField(blank=True, max_length=100, null=True, verbose_name='Author')),
                ('author_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Author')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d/%H/%M/%S', verbose_name='Image')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('title_sl', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('blurb', models.TextField(verbose_name='Blurb')),
                ('blurb_sl', models.TextField(null=True, verbose_name='Blurb')),
                ('blurb_en', models.TextField(null=True, verbose_name='Blurb')),
                ('link_to', models.URLField(blank=True, null=True, verbose_name='Link to')),
                ('link_to_sl', models.URLField(blank=True, null=True, verbose_name='Link to')),
                ('link_to_en', models.URLField(blank=True, null=True, verbose_name='Link to')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('body_sl', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('body_en', models.TextField(blank=True, null=True, verbose_name='Body')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-created', 'title'],
            },
        ),
    ]
