# Generated by Django 2.2.5 on 2019-10-22 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_delete_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
