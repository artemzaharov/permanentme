# Generated by Django 4.0.4 on 2022-04-14 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepage_banner_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='services',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
