# Generated by Django 4.1 on 2022-08-31 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usermessages", "0002_userfriendship"),
    ]

    operations = [
        migrations.DeleteModel(name="UserFriendship",),
    ]