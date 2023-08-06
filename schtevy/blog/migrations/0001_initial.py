# Generated by Django 4.2.4 on 2023-08-06 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Author',
                'ordering': ['nickname'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('mod_date', models.DateTimeField(verbose_name='date modified')),
                ('authors', models.ManyToManyField(to='blog.author')),
            ],
            options={
                'verbose_name_plural': 'Title',
                'ordering': ['mod_date'],
            },
        ),
    ]