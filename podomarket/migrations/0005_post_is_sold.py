# Generated by Django 4.2.3 on 2023-07-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0004_alter_post_item_condition_alter_post_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]
