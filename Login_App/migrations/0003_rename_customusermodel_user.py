# Generated by Django 4.2.7 on 2023-12-02 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Login_App', '0002_rename_user_customusermodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUserModel',
            new_name='User',
        ),
    ]