# Generated by Django 2.2.6 on 2019-12-10 08:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechnologyLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('text', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechnologyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('technology_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('years_of_experience', models.IntegerField(default=0)),
                ('months_of_experience', models.IntegerField(default=0)),
                ('not_want_to_use', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('technology_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technology.TechnologyLevel')),
                ('technology_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technology.TechnologyType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technologies', to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_type', models.CharField(blank=True, default='', max_length=256)),
                ('link', models.CharField(blank=True, default='', max_length=256)),
                ('technology', models.CharField(blank=True, default='', max_length=256)),
                ('text', models.TextField(default='')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('experience_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('experience_type', models.CharField(blank=True, default='', max_length=256)),
                ('link', models.CharField(blank=True, default='', max_length=256)),
                ('technology', models.CharField(blank=True, default='', max_length=256)),
                ('text', models.TextField(default='')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='user.User')),
            ],
        ),
    ]
