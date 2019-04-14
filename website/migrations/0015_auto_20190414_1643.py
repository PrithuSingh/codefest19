# Generated by Django 2.1.5 on 2019-04-14 11:13

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_handles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='handles',
            options={'verbose_name_plural': 'Handles'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='referral_code',
            field=models.CharField(default=website.models.generate_referral_code, max_length=50),
        ),
    ]