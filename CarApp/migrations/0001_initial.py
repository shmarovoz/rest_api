# Generated by Django 2.2.5 on 2019-10-02 22:33

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
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vim', models.CharField(db_index=True, max_length=60, unique=True, verbose_name='VIM')),
                ('color', models.CharField(max_length=60, verbose_name='Цвет')),
                ('brand', models.CharField(max_length=60, verbose_name='Марка')),
                ('model', models.CharField(choices=[(1, 'Хэчбек'), (1, 'Седан'), (1, 'Внедорожник'), (1, 'Универсал')], max_length=60)),
                ('owner', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
