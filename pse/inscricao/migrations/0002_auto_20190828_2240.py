# Generated by Django 2.2 on 2019-08-29 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='cpfcandidato',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='cpfresponsavel',
            field=models.IntegerField(),
        ),
    ]
