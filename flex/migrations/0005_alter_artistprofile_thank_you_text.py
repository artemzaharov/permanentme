# Generated by Django 4.0.4 on 2022-05-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0004_artistprofile_formfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistprofile',
            name='thank_you_text',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
