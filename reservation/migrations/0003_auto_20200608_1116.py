# Generated by Django 3.0.7 on 2020-06-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20200608_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='no_of_persons',
            new_name='age',
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(default='male', max_length=50),
        ),
    ]
