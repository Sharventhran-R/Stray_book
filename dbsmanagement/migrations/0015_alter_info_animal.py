# Generated by Django 4.1.4 on 2022-12-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbsmanagement', '0014_alter_info_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='animal',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Breed'),
        ),
    ]