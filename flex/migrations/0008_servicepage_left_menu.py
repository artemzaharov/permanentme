# Generated by Django 4.0.4 on 2022-05-07 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_leftmenu_homepage_left_menu'),
        ('flex', '0007_servicepage_button_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='left_menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.leftmenu'),
        ),
    ]