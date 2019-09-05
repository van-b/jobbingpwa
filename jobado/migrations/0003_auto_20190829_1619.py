# Generated by Django 2.2.4 on 2019-08-29 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobado', '0002_auto_20190829_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumuser',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='particuliers', to='jobado.District', verbose_name='quartier'),
        ),
    ]
