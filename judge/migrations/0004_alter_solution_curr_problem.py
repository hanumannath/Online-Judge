# Generated by Django 4.0.5 on 2022-07-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0003_alter_solution_curr_problem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='curr_problem',
            field=models.TextField(),
        ),
    ]