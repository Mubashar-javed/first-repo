# Generated by Django 2.2.5 on 2019-10-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20191017_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=10)),
            ],
        ),
    ]