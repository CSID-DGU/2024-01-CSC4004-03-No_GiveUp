# Generated by Django 5.0.4 on 2024-05-21 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_maxminnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('ID', models.CharField(max_length=50, unique=True)),
                ('user_mood', models.DecimalField(decimal_places=2, max_digits=4)),
                ('user_energy', models.CharField(max_length=50)),
                ('user_tempo', models.CharField(max_length=50)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
        ),
    ]