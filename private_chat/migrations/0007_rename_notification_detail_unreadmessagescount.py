# Generated by Django 4.0.2 on 2022-02-12 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_chat', '0006_rename_unreadmessagescount_detail_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='notification',
            new_name='unreadMessagesCount',
        ),
    ]
