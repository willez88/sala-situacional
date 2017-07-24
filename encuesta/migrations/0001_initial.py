# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 18:56
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta1', models.CharField(choices=[('a', 'Para generar nuevos derechos y deberes de los ciudadanos o mejorar los existentes'), ('b', 'Para mejorar los servicios públicos'), ('c', 'Para que el gobierno haga mejor su trabajo'), ('d', 'Para que la oposición haga mejor su trabajo')], max_length=1)),
                ('pregunta2', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1)),
                ('pregunta2_1', models.CharField(choices=[('a', 'Unico mecanismo para lograr la paz'), ('b', 'Solución a los problemas económicos'), ('c', 'Eliminar la inpunidad'), ('d', 'Gantizará los derechos sociales')], max_length=1)),
                ('pregunta2_2', models.CharField(choices=[('a', 'Es Ilegal'), ('b', 'No resuelve los problemas del país'), ('c', 'Temor por su trabajo'), ('d', 'Temor por  su vida'), ('e', 'Representa una patraña del gobierno')], max_length=1)),
                ('pregunta3', models.CharField(choices=[('a', 'Candidato del Oficialismo'), ('b', 'Candidato de la Oposición'), ('c', 'Candidato Independiente'), ('d', 'No votaría')], max_length=1)),
                ('telefono', models.CharField(help_text='Número telefónico de contacto con la persona', max_length=18, validators=[django.core.validators.RegexValidator('^\\(\\+058\\)-\\d{3}-\\d{7}$', "Número telefónico inválido. Solo se permiten números y los símbolos: '(', ')', '-', '+'")])),
                ('pregunta4', models.CharField(choices=[('a', '1.- Jehyson Jose Guzman Araque / Simon Pablo Figueroa'), ('b', '2.- Agustin Alexis Alvarez Tovar / Lorenza Ullan Severino'), ('c', '3.- Betty Carolina PeÑa Lopez'), ('d', '4.- Elias Rafael Sanchez Verde / Juan Carlos Lenzo'), ('e', '5.- Enrique Antonio Plata Ramirez / Teresa De Jesus Mora '), ('f', '6.- Nelsy Carolina Rivera Quinchoa'), ('g', '7.- Luis Carlos Perales Araque'), ('h', '8.- Johnny Rafael Andrade Barreto'), ('i', '9.- Jorge David Sandoval Rujano'), ('j', '10.- Gracian Claret Rondon Dezeo'), ('k', '11.- Greny Rosana Uzcategui Lacruz'), ('l', '12.- Hector Ramon Rojas Pernia'), ('m', '13.- Wilmer Arquimedes Iglesias Pino / Ramon David Fajardo Guanipa'), ('n', '14.- Alirio Jose Liscano '), ('o', '15.- Jose Rafael Luna ')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
