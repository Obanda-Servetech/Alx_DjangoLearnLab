# Generated by Django 5.1.6 on 2025-03-30 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(choices=[(True, 'Published'), (False, 'Draft')], default=False, help_text='Publish status of the post (Draft or Published).'),
        ),
    ]
