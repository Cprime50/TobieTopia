# Generated by Django 4.2.1 on 2023-05-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Enter your name here')),
                ('email', models.EmailField(max_length=254, verbose_name='Enter your Email here')),
                ('message', models.TextField(verbose_name='How can we help you?')),
            ],
        ),
    ]
