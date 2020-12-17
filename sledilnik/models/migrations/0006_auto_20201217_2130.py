# Generated by Django 3.1.4 on 2020-12-17 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_auto_20201217_2126'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PredictionIntervalType',
            new_name='PredictionIntervalKind',
        ),
        migrations.AlterModelOptions(
            name='predictionintervalkind',
            options={'ordering': ['name'], 'verbose_name': 'Prediction interval kind', 'verbose_name_plural': 'Prediction interval kinds'},
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='interval_type',
        ),
        migrations.AddField(
            model_name='prediction',
            name='interval_kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='models.predictionintervalkind', verbose_name='Interval kind'),
        ),
    ]
