# Generated by Django 4.1 on 2024-05-03 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('On The Way', 'On The Way'), ('Packed', 'Packed'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel')], default='Pending', max_length=50)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('payement', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.payement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
