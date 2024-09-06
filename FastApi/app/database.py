from dotenv import load_dotenv
from peewee import *
import os

load_dotenv()

database = MySQLDatabase(
    os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST')
)

class UserModel(Model):
    id = AutoField(primary_key = True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"

class OrderModel(Model):
    id = AutoField(primary_key = True)
    order_code = CharField(unique=True, max_length=30)
    user_id = ForeignKeyField(UserModel, related_name='orders')
    total = DecimalField(max_digits=10, decimal_places=2)
    order_date = DateField()
    state = CharField(max_length=15)

    class Meta:
        database = database
        table_name = "orders"

class LocationModel(Model):
    id = AutoField(primary_key = True)
    name = CharField(max_length=15)
    price = DecimalField(max_digits=10, decimal_places=2)
    max_capacity = IntegerField()
    available_seats = BooleanField()

    class Meta:
        database = database
        table_name = "locations"

class EventModel(Model):
    id = AutoField(primary_key = True)
    name = CharField(max_length=50)
    address = CharField(max_length=150)
    city = CharField(max_length=50)
    description = TextField()

    class Meta:
        database = database
        table_name = "events"

class ItemModel(Model):
    id = AutoField(primary_key = True)
    event = ForeignKeyField(EventModel, related_name='events')
    location = ForeignKeyField(LocationModel, related_name='locations')
    amount = IntegerField()
    unit_price = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        database = database
        table_name = "items"
