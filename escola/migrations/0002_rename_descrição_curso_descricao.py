# Generated by Django 3.2.7 on 2021-09-03 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='descrição',
            new_name='descricao',
        ),
    ]
