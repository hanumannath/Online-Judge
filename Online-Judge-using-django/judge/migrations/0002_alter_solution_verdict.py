# Generated by Django 4.0.5 on 2022-07-08 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='verdict',
            field=models.TextField(null=True),
        ),
    ]
