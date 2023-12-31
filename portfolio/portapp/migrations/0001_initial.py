# Generated by Django 4.2.5 on 2023-11-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=100)),
                ('comments', models.CharField(max_length=1000)),
                ('budget', models.CharField(choices=[('1', '10000'), ('2', '20000'), ('3', '30000+'), ('4', 'Less than 10000')], default='1', max_length=2)),
            ],
        ),
    ]
