# Generated by Django 4.1.3 on 2022-11-16 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0006_alter_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
