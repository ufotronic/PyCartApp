# Generated by Django 5.0.6 on 2024-07-20 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_reviewrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewrating',
            old_name='reviwe',
            new_name='review',
        ),
    ]