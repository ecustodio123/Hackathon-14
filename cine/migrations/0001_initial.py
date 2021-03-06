# Generated by Django 3.1.3 on 2020-11-08 22:14

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
            name='Cartelera',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=255)),
                ('horario', models.TimeField()),
                ('num_asientos', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'No disponible'), (1, 'Disponible')], default=1)),
            ],
            options={
                'verbose_name': 'Cartelera',
                'verbose_name_plural': 'Carteleras',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_tickets', models.IntegerField(default=1)),
                ('precio_pagar', models.IntegerField(default=20)),
                ('content', models.TextField()),
                ('published_date', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Inactivo'), (1, 'Activo')], default=1)),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('status', models.IntegerField(choices=[(0, 'No disponible'), (1, 'Disponible')], default=1)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('local', models.CharField(max_length=120)),
                ('slug_local', models.SlugField(max_length=255)),
                ('image_local', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/posts')),
                ('status', models.IntegerField(choices=[(0, 'Cerrado'), (1, 'Abierto')], default=1)),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locales',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/posts')),
                ('resumen', models.TextField()),
                ('release_date', models.DateField()),
                ('status', models.IntegerField(choices=[(0, 'No disponible'), (1, 'Disponible')], default=1)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.genero')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pelicula',
                'verbose_name_plural': 'Peliculas',
                'ordering': ['id'],
            },
        ),
        migrations.AddIndex(
            model_name='local',
            index=models.Index(fields=['local', 'status'], name='cine_local_local_61e4a3_idx'),
        ),
        migrations.AddIndex(
            model_name='genero',
            index=models.Index(fields=['name', 'status'], name='cine_genero_name_9db324_idx'),
        ),
        migrations.AddField(
            model_name='compra',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.local'),
        ),
        migrations.AddField(
            model_name='compra',
            name='pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.pelicula'),
        ),
        migrations.AddField(
            model_name='compra',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartelera',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.local'),
        ),
        migrations.AddField(
            model_name='cartelera',
            name='pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.pelicula'),
        ),
        migrations.AddIndex(
            model_name='pelicula',
            index=models.Index(fields=['title', 'slug', 'genero', 'user', 'status'], name='cine_pelicu_title_3a4c6e_idx'),
        ),
        migrations.AddIndex(
            model_name='compra',
            index=models.Index(fields=['pelicula', 'num_tickets', 'precio_pagar', 'content', 'local'], name='cine_compra_pelicul_75b213_idx'),
        ),
        migrations.AddIndex(
            model_name='cartelera',
            index=models.Index(fields=['pelicula', 'local', 'horario', 'status'], name='cine_cartel_pelicul_b26381_idx'),
        ),
    ]
