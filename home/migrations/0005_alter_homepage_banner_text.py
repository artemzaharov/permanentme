# Generated by Django 4.0.4 on 2022-04-14 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_bunner_button_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner_text',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
