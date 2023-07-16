# Generated by Django 4.2.3 on 2023-07-16 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WeatherApp', '0002_user_password_confirmation'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WeatherApp.user')),
            ],
        ),
    ]