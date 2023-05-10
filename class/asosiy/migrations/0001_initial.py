# Generated by Django 4.2.1 on 2023-05-08 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_f_o', models.CharField(max_length=100)),
                ('clas', models.SmallIntegerField()),
                ('number', models.CharField(max_length=14)),
                ('social_network', models.CharField(max_length=1000)),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.img')),
            ],
        ),
        migrations.CreateModel(
            name='InfoStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.img')),
            ],
        ),
    ]