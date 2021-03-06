# Generated by Django 3.0.1 on 2020-01-08 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0002_auto_20200108_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Restaurant')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='Review_Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField()),
            ],
            options={
                'db_table': 'review_stars',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kakao', models.IntegerField(null=True)),
                ('facebook', models.IntegerField(null=True)),
                ('nick_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='User_Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Restaurant')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'user_likes',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='like_user',
            field=models.ManyToManyField(through='user.User_Like', to='restaurant.Restaurant'),
        ),
        migrations.CreateModel(
            name='Review_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(max_length=4500)),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Review')),
            ],
            options={
                'db_table': 'review_images',
            },
        ),
        migrations.AddField(
            model_name='review',
            name='reveiw_start',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Review_Star'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User'),
        ),
    ]
