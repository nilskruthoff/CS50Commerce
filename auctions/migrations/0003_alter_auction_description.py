# Generated by Django 4.0.2 on 2022-02-16 23:43

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
