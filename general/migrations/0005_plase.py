# Generated by Django 3.0.2 on 2020-01-16 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_delete_fontphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('title', models.CharField(max_length=200)),
                ('post_title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
