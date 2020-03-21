# Generated by Django 3.0.2 on 2020-03-21 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utils', '0003_area_group_groupfield'),
        ('backend', '0013_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(verbose_name='fecha de inventario')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.Area', verbose_name='area de levantamiento')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.PositiveSmallIntegerField(choices=[(1, 'Encontrado'), (2, 'No encontrado')], default=2)),
                ('comments', models.CharField(blank=True, max_length=250, null=True, verbose_name='comentarios')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Active')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Inventory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
        migrations.CreateModel(
            name='UnActive',
            fields=[
            ],
            options={
                'verbose_name': 'orden de baja',
                'verbose_name_plural': 'dar de baja',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('backend.translate',),
        ),
        migrations.AlterField(
            model_name='translate',
            name='document_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Orden de compra'), (2, 'Orden de entrada'), (3, 'Orden de salida'), (4, 'Mantenimiento'), (5, 'Baja')], null=True),
        ),
    ]
