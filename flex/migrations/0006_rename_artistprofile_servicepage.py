# Generated by Django 4.0.4 on 2022-05-07 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('flex', '0005_alter_artistprofile_thank_you_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArtistProfile',
            new_name='ServicePage',
        ),
    ]
