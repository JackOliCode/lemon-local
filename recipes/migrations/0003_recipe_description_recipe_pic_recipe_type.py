# Generated by Django 4.2.4 on 2023-08-31 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_remove_recipe_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='This recipe looks delicious!', max_length=200),
        ),
        migrations.AddField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='recipes'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack'), ('drink', 'Drink')], default='Snack', max_length=40),
        ),
    ]