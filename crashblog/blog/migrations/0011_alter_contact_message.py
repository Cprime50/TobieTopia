# Generated by Django 4.2.1 on 2023-05-29 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='How may be of help to you?'),
        ),
    ]
