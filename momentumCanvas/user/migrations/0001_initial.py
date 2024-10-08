# Generated by Django 5.1.1 on 2024-09-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('leetcode', models.CharField(default=None, max_length=500)),
                ('codechef', models.CharField(default=None, max_length=500)),
                ('geekforgeeks', models.CharField(default=None, max_length=500)),
                ('codeforces', models.CharField(default=None, max_length=500)),
                ('github', models.CharField(default=None, max_length=500)),
            ],
        ),
    ]
