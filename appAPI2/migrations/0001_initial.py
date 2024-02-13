# Generated by Django 4.1.13 on 2024-02-13 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patinete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
                ('tipo', models.CharField(max_length=50)),
                ('precio_desbloqueo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('precio_minuto', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debito', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_desbloqueo', models.DateTimeField()),
                ('fecha_entrega', models.DateTimeField(blank=True, null=True)),
                ('coste_final', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('patinete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appAPI2.patinete')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]