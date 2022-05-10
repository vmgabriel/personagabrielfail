# Generated by Django 3.2.7 on 2021-10-05 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.AddField(
            model_name='user',
            name='inactive_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]