# Generated by Django 3.1.3 on 2020-11-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20201114_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='option1_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='option2_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='option3_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='option4_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
