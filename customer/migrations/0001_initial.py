# Generated by Django 2.1.2 on 2018-10-19 09:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='issues',
            fields=[
                ('issues_id', models.CharField(default='0', max_length=10, primary_key=True, serialize=False)),
                ('order_id', models.CharField(default='0', max_length=10)),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('writer_id', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.CharField(default='0', max_length=10, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('track_id', models.CharField(max_length=20)),
                ('r_address', models.CharField(max_length=50)),
                ('s_address', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
                ('r_phone', models.CharField(max_length=20)),
                ('s_phone', models.CharField(max_length=20)),
                ('receiver', models.CharField(max_length=20)),
                ('sender', models.CharField(max_length=20)),
                ('weight', models.CharField(max_length=20)),
                ('s_postcode', models.CharField(max_length=20)),
                ('r_postcode', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('box_id', models.CharField(max_length=20)),
                ('company_id', models.CharField(max_length=20)),
                ('delivery_staff', models.CharField(max_length=20)),
            ],
        ),
    ]
