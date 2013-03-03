# Generated by Django 3.1.6 on 2021-02-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
                ('completed_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
