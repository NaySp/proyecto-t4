# Generated by Django 5.0.3 on 2024-03-26 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radicate', models.CharField(max_length=20)),
                ('payment_order_code', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('cost_center', models.CharField(max_length=20)),
                ('name', models.CharField(default='', max_length=40)),
                ('identificationNumber', models.CharField(default='', max_length=10)),
                ('dependency', models.CharField(max_length=30)),
                ('destiny_city', models.CharField(max_length=30)),
                ('travel_date', models.DateField()),
                ('return_date', models.DateField()),
                ('motive', models.TextField()),
                ('foreign_money', models.BooleanField()),
                ('money', models.CharField(max_length=10)),
                ('last_day_at_icesi', models.DateField()),
                ('elaborator_name', models.CharField(max_length=20)),
                ('orderer_name', models.CharField(max_length=20)),
                ('bank', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('saving', 'De ahorros'), ('current', 'Corriente')], max_length=10)),
                ('account_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Charge_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('identification', models.CharField(default='', max_length=10)),
                ('phone', models.CharField(default='', max_length=13)),
                ('city', models.CharField(max_length=20)),
                ('addres', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('value_letters', models.CharField(max_length=60)),
                ('value_numbers', models.CharField(max_length=15)),
                ('concept', models.TextField()),
                ('bank', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('De ahorros', 'De ahorros'), ('Corriente', 'Corriente')], max_length=10)),
                ('account_number', models.CharField(max_length=20)),
                ('cex', models.CharField(max_length=20)),
                ('retentions', models.BooleanField()),
                ('declarant', models.BooleanField()),
                ('colombian_resident', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Exterior_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary_name', models.CharField(max_length=20)),
                ('beneficiary_last_name', models.CharField(max_length=20)),
                ('beneficiary_document_type', models.CharField(max_length=10)),
                ('beneficiary_document_no', models.CharField(max_length=20)),
                ('passport_number', models.CharField(max_length=20)),
                ('passport_expedition_city', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('bank_name', models.CharField(max_length=20)),
                ('account_type', models.CharField(max_length=10)),
                ('swift_code', models.CharField(max_length=10)),
                ('iban_aba_code_type', models.CharField(max_length=10)),
                ('iban_aba_code', models.CharField(max_length=10)),
                ('account_name', models.CharField(max_length=30)),
                ('account_number', models.CharField(max_length=20)),
                ('bank_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('pendiente de aceptación', 'Pendiente de aceptación'), ('en revisión', 'En revisión'), ('revisado', 'Revisado'), ('aprovado', 'Aprobado'), ('aceptado', 'Aceptado'), ('Rechazado por contabilidad', 'Rechazado por contabilidad')], max_length=30)),
                ('color', models.CharField(choices=[('gray', 'Gris'), ('orange', 'Naranja'), ('yellow', 'Amarillo'), ('green', 'Verde'), ('blue', 'Azul'), ('red', 'Rojo')], max_length=10)),
                ('creation_date', models.DateField()),
                ('type', models.CharField(max_length=20)),
                ('concept', models.TextField()),
                ('money_type', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('cenco', models.CharField(max_length=20)),
                ('cex_number', models.CharField(max_length=20)),
                ('observations', models.TextField()),
                ('close_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Legalization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legalization_date', models.DateField()),
                ('cost_center', models.CharField(max_length=30)),
                ('name', models.CharField(default='', max_length=40)),
                ('identificationNumber', models.CharField(default='', max_length=10)),
                ('dependency', models.CharField(max_length=30)),
                ('destiny', models.CharField(max_length=20)),
                ('travel_date', models.DateField()),
                ('return_date', models.DateField()),
                ('motive', models.TextField()),
                ('value', models.IntegerField()),
                ('employee_balance', models.IntegerField()),
                ('icesi_balance', models.IntegerField()),
                ('descount_in_one_quote', models.BooleanField()),
                ('elaborator_name', models.CharField(max_length=20)),
                ('orderer_name', models.CharField(max_length=20)),
                ('bank', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('saving', 'De ahorros'), ('current', 'Corriente')], max_length=10)),
                ('account_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radicate', models.CharField(max_length=20)),
                ('payment_order_code', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('name', models.CharField(default='', max_length=40)),
                ('idNumber', models.CharField(default='', max_length=10)),
                ('charge', models.CharField(default='', max_length=40)),
                ('dependency', models.CharField(default='', max_length=40)),
                ('cenco', models.CharField(max_length=20)),
                ('value', models.DecimalField(decimal_places=10, max_digits=20)),
                ('concept', models.TextField()),
                ('description', models.TextField()),
                ('bank', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('saving', 'De ahorros'), ('current', 'Corriente')], max_length=10)),
                ('account_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Expense_balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value', models.DecimalField(decimal_places=10, max_digits=20)),
                ('advance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaContableApp.advance')),
            ],
        ),
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comments', models.TextField()),
                ('assigned_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaContableApp.following')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('support_no', models.IntegerField()),
                ('third_person_name', models.CharField(max_length=30)),
                ('third_person_nit', models.CharField(max_length=20)),
                ('concept', models.TextField()),
                ('money', models.CharField(max_length=10)),
                ('value', models.DecimalField(decimal_places=10, max_digits=20)),
                ('legalization_facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaContableApp.legalization')),
            ],
        ),
    ]
