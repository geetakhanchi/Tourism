# Generated by Django 4.0.3 on 2022-04-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourisms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourism',
            name='agent',
            field=models.TextField(),
        ),
    ]
