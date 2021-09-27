# Generated by Django 3.2.7 on 2021-09-21 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField(max_length=20)),
                ('cpassword', models.TextField(max_length=20)),
                ('address', models.TextField(max_length=999)),
            ],
        ),
        migrations.DeleteModel(
            name='info',
        ),
    ]
