# Generated by Django 3.1.3 on 2021-05-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_post_snippets'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_header',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippets',
            field=models.CharField(max_length=250),
        ),
    ]
