# Generated by Django 3.2.18 on 2023-03-03 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_user_comment_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='introduction',
            field=models.CharField(default='this is the introduction', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]
