# Generated by Django 4.2.2 on 2023-06-20 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albumns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='mp3_file',
            field=models.FileField(blank=True, null=True, upload_to='songs/mp3'),
        ),
    ]