# Generated by Django 5.0.2 on 2024-03-31 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('retentions', models.BooleanField(default=False)),
                ('declarant', models.BooleanField(default=False)),
                ('colombian_resident', models.BooleanField(default=False)),
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
                ('account_type', models.CharField(choices=[('Ahorros', 'Ahorros'), ('Corriente', 'Corriente')], max_length=10)),
                ('swift_code', models.CharField(max_length=10)),
                ('iban_aba_code_type', models.CharField(choices=[('IBAN', 'IBAN'), ('ABA', 'ABA')], max_length=10)),
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
                ('creationDate', models.DateField()),
                ('creator', models.CharField(max_length=40, null=True)),
                ('type', models.CharField(max_length=20)),
                ('supplier', models.CharField(max_length=40, null=True)),
                ('supplierId', models.CharField(max_length=10, null=True)),
                ('documentNumber', models.CharField(max_length=10, null=True)),
                ('manager', models.CharField(max_length=40, null=True)),
                ('acceptor', models.CharField(max_length=40, null=True)),
                ('revisor', models.CharField(max_length=40, null=True)),
                ('acceptanceState', models.CharField(max_length=10, null=True)),
                ('acceptanceDate', models.DateField(null=True)),
                ('revisionState', models.CharField(max_length=10, null=True)),
                ('revision', models.CharField(max_length=40, null=True)),
                ('concept', models.TextField()),
                ('supplierEmail', models.EmailField(max_length=254, null=True)),
                ('moneyType', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('cenco', models.CharField(max_length=20)),
                ('cexNumber', models.CharField(max_length=20)),
                ('observations', models.TextField()),
                ('revisionDate', models.DateField(null=True)),
                ('approvalState', models.CharField(max_length=10, null=True)),
                ('approval', models.TextField(null=True)),
                ('approvalDate', models.DateField(null=True)),
                ('approvalComments', models.TextField(null=True)),
                ('accountingReception', models.CharField(max_length=10, null=True)),
                ('accountingComments', models.TextField(null=True)),
                ('accountingDate', models.DateField(null=True)),
                ('receptor', models.CharField(max_length=40, null=True)),
                ('modificationDate', models.DateField(null=True)),
                ('modifier', models.CharField(max_length=40, null=True)),
                ('closeDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('beneficiaryName', models.CharField(default='', max_length=40)),
                ('idNumber', models.CharField(default='', max_length=10)),
                ('charge', models.CharField(default='', max_length=40)),
                ('dependency', models.CharField(default='', max_length=40)),
                ('cenco', models.CharField(max_length=20)),
                ('value', models.DecimalField(decimal_places=10, max_digits=30)),
                ('concept', models.CharField(choices=[('Reintegro colaboradores', 'Reintegro colaboradores'), ('Patrocinio estudiantes', 'Patrocinio estudiantes'), ('Beca pasantia', 'Beca pasantia'), ('Evento de estudiantes', 'Evento de estudiantes'), ('Pago alimentación estudiante extranjero', 'Pago alimentación estudiante extranjero'), ('En la descripción', 'En la descripción')], max_length=40)),
                ('description', models.TextField()),
                ('radicate', models.CharField(max_length=20)),
                ('payment_order_code', models.CharField(max_length=20)),
                ('paymentMethod', models.CharField(choices=[('Nomina', 'Nomina'), ('Consignación', 'Consignación')], max_length=15)),
                ('typeAccount', models.CharField(choices=[('De ahorros', 'De ahorros'), ('Corriente', 'Corriente')], max_length=10)),
                ('account_number', models.CharField(max_length=20)),
                ('authorName', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state', models.CharField(choices=[('pendiente de aceptación', 'Pendiente de aceptación'), ('en revisión', 'En revisión'), ('revisado', 'Revisado'), ('aprobado', 'Aprobado'), ('aceptado', 'Aceptado'), ('Rechazado por contabilidad', 'Rechazado por contabilidad')], max_length=30, primary_key=True, serialize=False)),
                ('color', models.CharField(choices=[('gray', 'Gris'), ('orange', 'Naranja'), ('yellow', 'Amarillo'), ('green', 'Verde'), ('blue', 'Azul'), ('red', 'Rojo')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AttachedDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('associatedFollowing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaContableApp.following')),
            ],
        ),
        migrations.AddField(
            model_name='following',
            name='currentState',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SistemaContableApp.state'),
        ),
    ]
