# Generated by Django 4.2.4 on 2023-10-02 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='choices',
            field=models.ManyToManyField(to='polls.choice'),
        ),
    ]
