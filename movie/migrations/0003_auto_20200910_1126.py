# Generated by Django 3.1.1 on 2020-09-10 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='alt_zh_names',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(db_index=True),
        ),
    ]