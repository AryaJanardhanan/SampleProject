# Generated by Django 5.1 on 2024-08-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_item_remove_stuprofile_student_delete_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
