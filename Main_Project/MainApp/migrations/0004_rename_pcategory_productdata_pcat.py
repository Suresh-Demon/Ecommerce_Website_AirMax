# Generated by Django 5.0.7 on 2024-07-27 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_alter_productdata_pimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdata',
            old_name='pcategory',
            new_name='pcat',
        ),
    ]
