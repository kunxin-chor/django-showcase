# Generated by Django 2.2.4 on 2019-08-07 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_item_completed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='completed_at',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]