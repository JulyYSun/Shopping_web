# Generated by Django 2.0.4 on 2018-06-26 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='产品别表',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('名称', models.CharField(max_length=50, unique=True)),
                ('描述', models.TextField(blank=True)),
                ('图片', models.ImageField(blank=True, null=True, upload_to='category')),
                ('价格', models.DecimalField(decimal_places=2, max_digits=10)),
                ('库存', models.IntegerField(default=0)),
                ('已上架', models.BooleanField(default=True)),
                ('创建时间', models.DateTimeField(auto_now_add=True)),
                ('修改时间', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '产品列表',
                'db_table': '产品列表',
                'ordering': ('创建时间',),
            },
        ),
        migrations.CreateModel(
            name='商品类别表',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('名称', models.CharField(max_length=50, unique=True)),
                ('描述', models.TextField(blank=True)),
                ('图片', models.ImageField(blank=True, null=True, upload_to='category')),
            ],
            options={
                'verbose_name_plural': '商品类别表',
                'db_table': '商品类别表',
            },
        ),
        migrations.AddField(
            model_name='产品别表',
            name='所属类别',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.商品类别表'),
        ),
    ]
