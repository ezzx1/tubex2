# Generated by Django 4.2.3 on 2023-08-12 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0004_alter_department_options_alter_emp_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='name',
            new_name='الاسم',
        ),
        migrations.RenameField(
            model_name='emp',
            old_name='dep',
            new_name='القطاع',
        ),
        migrations.RenameField(
            model_name='emp',
            old_name='salary',
            new_name='المرتب',
        ),
    ]
