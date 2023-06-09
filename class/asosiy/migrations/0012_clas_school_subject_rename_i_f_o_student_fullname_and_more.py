# Generated by Django 4.2.1 on 2023-05-17 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asosiy', '0011_alter_student_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('clas', models.SmallIntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='i_f_o',
            new_name='fullname',
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_bearth',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.img')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.school')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudyTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_lesson', models.TimeField()),
                ('end_lesson', models.TimeField()),
                ('clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.clas')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.SmallIntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.subject')),
            ],
        ),
        migrations.AddField(
            model_name='clas',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.school'),
        ),
        migrations.AddField(
            model_name='clas',
            name='students',
            field=models.ManyToManyField(related_name='classes', to='asosiy.student'),
        ),
        migrations.AddField(
            model_name='clas',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.teacher'),
        ),
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asosiy.school'),
        ),
    ]
