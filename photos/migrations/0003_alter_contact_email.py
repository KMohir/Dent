# Generated by Django 3.2.3 on 2022-11-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]