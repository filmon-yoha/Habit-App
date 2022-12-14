# Generated by Django 4.0.3 on 2022-07-28 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HabitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.CharField(choices=[('DAILY', 'DAILY'), ('WEEKLY', 'WEEKLY'), ('MONTHLY', 'MONTHLY')], default=(('DAILY', 'DAILY'),), max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
            ],
            options={
                'db_table': 'habit',
            },
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('task_date', models.DateField()),
                ('habit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habit_tracker.habitmodel')),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
