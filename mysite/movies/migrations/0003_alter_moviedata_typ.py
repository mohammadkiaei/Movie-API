# Generated by Django 4.1 on 2022-09-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_typ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='typ',
            field=models.CharField(default='Action', max_length=200),
        ),
    ]
