# Generated by Django 3.1.3 on 2020-11-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.DecimalField(decimal_places=0, max_digits=6)),
                ('content', models.TextField()),
            ],
        ),
    ]
