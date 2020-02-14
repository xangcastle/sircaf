# Generated by Django 3.0.2 on 2020-02-14 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
        ('backend', '0008_auto_20200214_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='active',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.Brand', verbose_name='marca'),
        ),
        migrations.AlterField(
            model_name='active',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.Status', verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='area',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.Country', verbose_name='pais'),
        ),
        migrations.AlterField(
            model_name='translateitem',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.Status', verbose_name='estado'),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
