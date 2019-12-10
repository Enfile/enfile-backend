# Generated by Django 2.2.6 on 2019-12-10 07:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('icon_path', models.CharField(blank=True, max_length=256, null=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('sex', models.IntegerField(default=0)),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('school_year', models.IntegerField(blank=True, null=True)),
                ('school_name', models.CharField(blank=True, max_length=256, null=True)),
                ('profile', models.CharField(blank=True, max_length=256, null=True)),
                ('using_os', models.CharField(blank=True, max_length=256, null=True)),
                ('link', models.CharField(blank=True, max_length=256, null=True)),
                ('contact', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
        ),
    ]
