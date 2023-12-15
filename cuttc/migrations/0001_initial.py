# Generated by Django 4.2 on 2023-12-15 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_url', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_click', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Redirects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redirect_url', models.CharField(max_length=1500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('base_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='url', to='cuttc.urls')),
            ],
        ),
    ]