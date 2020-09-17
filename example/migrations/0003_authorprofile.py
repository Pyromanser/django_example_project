# Generated by Django 3.1.1 on 2020-09-07 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_auto_20200907_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(help_text='Author bio', max_length=1000, verbose_name='about')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='example.author')),
            ],
        ),
    ]