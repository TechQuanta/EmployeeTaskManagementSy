# Generated by Django 4.2.5 on 2024-04-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ETMDAPP", "0010_alter_employee_newemail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="newemail",
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
