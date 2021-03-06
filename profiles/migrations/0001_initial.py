# Generated by Django 3.1.1 on 2020-10-11 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('age', models.DateField(blank=True, null=True)),
                ('Hobbies', models.CharField(blank=True, max_length=200)),
                ('work', models.CharField(blank=True, max_length=200)),
                ('education', models.CharField(blank=True, max_length=40)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=7)),
                ('relationship', models.CharField(blank=True, choices=[('Single', 'Single'), ('In a relatinship', 'In a relatinship'), ('Engaged', 'Engaged'), ('Married', 'Married'), ("It's complicated", "It's complicated"), ('Divored', 'Divored'), ('Widowed', 'Widowed'), ('In an open relationship', 'In an open relationship')], max_length=23)),
                ('about', models.TextField(blank=True, default='No Bio')),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, default='user/happy.jpg', upload_to='user/cover')),
                ('picture', models.ImageField(blank=True, default='user/User.jpg', upload_to='user')),
                ('country', models.CharField(blank=True, max_length=20)),
                ('friends', models.ManyToManyField(blank=True, to='profiles.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='profiles.profile')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followings', to='profiles.profile')),
            ],
            options={
                'unique_together': {('follower', 'following')},
            },
        ),
    ]
