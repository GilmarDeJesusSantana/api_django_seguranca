# Generated by Django 4.0.3 on 2022-03-23 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_aluno_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]