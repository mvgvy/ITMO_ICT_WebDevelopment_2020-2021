# Generated by Django 3.1.5 on 2021-01-12 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CleaningParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('mon', 'Понедельник'), ('tue', 'Вторник'), ('wed', 'Среда'), ('thu', 'Четверг'), ('fri', 'Пятница'), ('sat', 'Суббота'), ('sun', 'Воскресенье')], max_length=30)),
                ('floor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('type', models.CharField(choices=[('one', 'одноместный'), ('two', 'двухместный'), ('three', 'трехместный')], default='one', max_length=15)),
                ('price', models.IntegerField(verbose_name='Price per day')),
                ('phone', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('busy', 'занят'), ('free', 'свободен')], default='free', max_length=15)),
                ('total', models.IntegerField(default=0, verbose_name='Total income')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StaffCleaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('params', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppHotel.cleaningparams')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppHotel.staff')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='cleaning',
            field=models.ManyToManyField(through='AppHotel.StaffCleaning', to='AppHotel.CleaningParams'),
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport', models.IntegerField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('room', models.ForeignKey(limit_choices_to={'status': 'free'}, on_delete=django.db.models.deletion.CASCADE, to='AppHotel.room')),
            ],
        ),
    ]
