# Generated by Django 2.1.2 on 2018-10-24 06:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0002_auto_20181021_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='issue',
            fields=[
                ('issue_id', models.CharField(default='1', max_length=10, primary_key=True, serialize=False)),
                ('order_id', models.CharField(default='0', max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='wait', max_length=20)),
            ],
        ),
    ]
