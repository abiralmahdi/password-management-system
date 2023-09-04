# Generated by Django 3.2.13 on 2023-02-21 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20230221_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(default='', max_length=1000)),
                ('email', models.CharField(default='', max_length=1000)),
                ('password', models.CharField(default='', max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
