# Generated by Django 2.1.5 on 2019-01-28 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("brutaldon", "0019_auto_20190124_0813")]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="note_seen",
            field=models.CharField(blank=True, max_length=128, null=True),
        )
    ]