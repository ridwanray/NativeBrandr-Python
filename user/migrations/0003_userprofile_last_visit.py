# Generated by Django 2.1 on 2019-04-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190409_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_visit',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]