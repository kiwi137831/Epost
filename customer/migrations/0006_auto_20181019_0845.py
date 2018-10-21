# Generated by Django 2.1 on 2018-10-19 08:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20181019_0845'),
        ('customer', '0005_auto_20181015_0236'),
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
                ('status', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='1', max_length=10, primary_key=True, serialize=False),
        ),
    ]
