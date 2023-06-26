# Generated by Django 4.2.2 on 2023-06-26 20:06

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
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('start_time', models.TimeField(blank=True, default=None, null=True)),
                ('end_time', models.TimeField(blank=True, default=None, null=True)),
                ('address', models.CharField(max_length=30)),
                ('start_date', models.DateField(blank=True, default=None, null=True)),
                ('end_date', models.DateField(blank=True, default=None, null=True)),
                ('category_univ', models.CharField(max_length=50)),
                ('category_type', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='benefits/')),
                ('benefit_like_count', models.PositiveIntegerField(default=0)),
                ('benefit_rate_average', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('benefit_like', models.ManyToManyField(blank=True, related_name='benefit_likes', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefit_rate', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('comment_like_count', models.IntegerField(default=0)),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='benefits.benefit')),
                ('comment_like', models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
