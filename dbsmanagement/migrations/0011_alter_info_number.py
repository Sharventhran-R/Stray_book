# Generated by Django 4.1.4 on 2022-12-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbsmanagement', '0010_alter_info_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
