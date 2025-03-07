# Generated by Django 5.1.6 on 2025-02-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=50)),
                ('font_color', models.CharField(max_length=50)),
                ('bg_color', models.CharField(max_length=50)),
                ('dark_font_color', models.CharField(max_length=50)),
                ('dark_bg_color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('end_date', models.CharField(blank=True, max_length=7)),
                ('is_done', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(blank=True, to='tasks.category')),
            ],
        ),
    ]
