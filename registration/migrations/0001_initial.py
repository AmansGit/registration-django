# Generated by Django 2.2 on 2020-09-05 06:55

from django.db import migrations, models
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=registration.models.user_image)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=200, null=True)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]