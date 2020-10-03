# Generated by Django 3.1.1 on 2020-09-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField(default=0)),
                ('p_name', models.CharField(max_length=100)),
                ('p_price', models.FloatField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(max_length=100)),
                ('p_image', models.ImageField(upload_to='product/images')),
            ],
        ),
    ]
