# Generated by Django 5.0.4 on 2024-04-26 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_remove_contacts_twitter_contacts_instagram_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='whapsapp',
            new_name='whatsapp',
        ),
    ]