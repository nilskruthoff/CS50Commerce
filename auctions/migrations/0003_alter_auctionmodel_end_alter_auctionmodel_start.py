# Generated by Django 4.0.2 on 2022-02-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_auctionmodel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionmodel',
            name='end',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='auctionmodel',
            name='start',
            field=models.DateField(default=None),
        ),
    ]
