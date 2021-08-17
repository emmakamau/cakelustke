# Generated by Django 3.2.6 on 2021-08-15 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakelust', '0005_auto_20210815_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cakesize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cakesize', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Priceguide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cakeprice', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='caketype',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='description',
        ),
        migrations.AlterField(
            model_name='review',
            name='custreview',
            field=models.TextField(max_length=400),
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caketype', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('cakeprice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cakelust.priceguide')),
                ('cakesize', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cakelust.cakesize')),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='cakedesc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cakedesc', to='cakelust.cake'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='cakename',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cakename', to='cakelust.cake'),
        ),
    ]
