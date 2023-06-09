# Generated by Django 4.1.7 on 2023-03-31 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Garagem', '0006_cor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acessorio',
            options={'verbose_name_plural': 'Acessórios'},
        ),
        migrations.AlterModelOptions(
            name='cor',
            options={'verbose_name_plural': 'Cores'},
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=0, null=True)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculo', to='Garagem.categoria')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculo', to='Garagem.cor')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculo', to='Garagem.marca')),
            ],
            options={
                'verbose_name_plural': 'Cores',
            },
        ),
    ]
