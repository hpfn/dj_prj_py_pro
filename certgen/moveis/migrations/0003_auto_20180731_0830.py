# Generated by Django 2.0.7 on 2018-07-31 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moveis', '0002_auto_20180731_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movel',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movel',
            name='ultima_atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]