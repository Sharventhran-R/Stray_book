# Generated by Django 4.1.4 on 2022-12-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbsmanagement', '0006_alter_info_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='name',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Name'),
        ),
    ]