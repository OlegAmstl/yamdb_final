# Generated by Django 2.2.16 on 2022-06-15 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_account_balance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('change_task_status', 'Can change the status of tasks')]},
        ),
    ]