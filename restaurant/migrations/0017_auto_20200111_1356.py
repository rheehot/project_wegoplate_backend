# Generated by Django 3.0.1 on 2020-01-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0016_topic_top_lists_topics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='top_lists_topics',
        ),
        migrations.AddField(
            model_name='top_list',
            name='top_lists_topics',
            field=models.ManyToManyField(through='restaurant.Topic_Top_list', to='restaurant.Topic'),
        ),
    ]
