# Generated by Django 4.2.2 on 2023-06-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_profile_facebook_līnk_profile_github_līnk_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
