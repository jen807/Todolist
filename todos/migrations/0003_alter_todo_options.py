# Generated by Django 5.1.6 on 2025-02-27 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_created_at_todo_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name_plural': '할일'},
        ),
    ]
