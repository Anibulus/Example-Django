# Generated by Django 3.2.7 on 2021-09-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('passw', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('is_admin', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
