# Generated by Django 4.2.3 on 2023-08-12 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'قطاعات'},
        ),
        migrations.AlterModelOptions(
            name='emp',
            options={'verbose_name': 'موظفين'},
        ),
        migrations.RenameField(
            model_name='emp',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='last_name',
        ),
    ]
