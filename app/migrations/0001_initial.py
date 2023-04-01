# Generated by Django 4.1.7 on 2023-04-01 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dept",
            fields=[
                (
                    "dept_name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("dept_no", models.IntegerField(unique=True)),
                ("dept_loc", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Emp",
            fields=[
                ("emp_no", models.IntegerField(unique=True)),
                (
                    "emp_name",
                    models.CharField(max_length=122, primary_key=True, serialize=False),
                ),
                (
                    "dept_no",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.dept"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Family",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("f_no", models.IntegerField()),
                (
                    "emp_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.emp"
                    ),
                ),
            ],
        ),
    ]
