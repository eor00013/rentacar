
from api.models.city import City
from api.models import Model, Brand, Order, Car, Category
from django.core.management import BaseCommand
import json
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import requests
import os

class Command(BaseCommand):

    def handle(self, *args, **options):

        def clean_all_db():
            print("Cleaning DB")
            Order.objects.all().delete()
            Car.objects.all().delete()
            City.objects.all().delete()
            Model.objects.all().delete()
            Brand.objects.all().delete()
            Category.objects.all().delete()
            User.objects.all().delete()

        def insert_users():
            print("Inserting super user...")
            username = "root"
            email = "superuser@email.com"
            password = "12345"
            user_django = User.objects.create_superuser(
                username=username, email=email, password=password)
            user_django.save()

        def insert_brands():
            print("Inserting brands...")
            with open('data/brands.json', 'r') as f:
                brands_str = f.read()
                brands_json = json.loads(brands_str)

            for brand_json in brands_json:
                brand = Brand()
                brand.pk = brand_json.get('pk')
                brand.name = brand_json.get('name')
                brand.save()

        def insert_models():
            print("Inserting models...")
            with open('data/models.json', 'r') as f:
                models_str = f.read()
                models_json = json.loads(models_str)

            for model_json in models_json:
                model = Model()
                model.pk = model_json.get('pk')
                model.name = model_json.get('name')
                model.year = model_json.get('year')
                model.brand = Brand.objects.get(pk=model_json.get('brand'))
                model.save()

                req = requests.get(model_json.get('photo'))
                if req.status_code == 200:
                    img_temp = NamedTemporaryFile()
                    img_temp.write(req.content)
                    img_temp.flush()
                    model.photo.save(os.path.basename(
                        model_json.get('photo')), File(img_temp), save=True)        

        def insert_categories():
            print("Inserting categories...")
            with open('data/categories.json', 'r') as f:
                categories_str = f.read()
                categories_json = json.loads(categories_str)

            for category_json in categories_json:
                category = Category()
                category.pk = category_json.get('pk')
                category.name = category_json.get('name')
                category.price = category_json.get('price')
                category.save()

        def insert_cars():
            print("Inserting cars...")
            with open('data/cars.json', 'r') as f:
                cars_str = f.read()
                cars_json = json.loads(cars_str)

            for car_json in cars_json:
                car = Car()
                car.color_type = car_json.get('color_type')
                car.doors = car_json.get('doors')
                car.passengers = car_json.get('passengers')
                car.registration = car_json.get('registration')
                car.fuel_type = car_json.get('fuel_type')
                car.category = Category.objects.get(
                    pk=car_json.get('category'))
                car.model = Model.objects.get(pk=car_json.get('model'))
                car.city = City.objects.get(pk=car_json.get('city'))
                car.save()

        def insert_cities():
            print("Inserting cities...")
            with open('data/cities.json', 'r') as f:
                cities_str = f.read()
                cities_json = json.loads(cities_str)

            for city_json in cities_json:
                city = City()
                city.pk = city_json.get('pk')
                city.name = city_json.get('name')
                city.save()

        ########################################################
        # Insert all data
        ########################################################
        clean_all_db()
        insert_users()
        print()
        insert_cities()
        print()
        insert_brands()
        print()
        insert_models()
        print()
        insert_categories()
        print()
        insert_cars()
        print("Insert data successful 👌👌👌")
