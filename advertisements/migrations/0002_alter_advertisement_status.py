# Generated by Django 4.1.7 on 2023-03-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.TextField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN'),
        ),
    ]
