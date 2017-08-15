from mongoengine import Document
from mongoengine import fields

# Create your models here.

class test(Document):
    goods_id = fields.IntField()
    sold_timestamp = fields.IntField()
    sold_price = fields.FloatField()

class Sales(Document):
    sold_month = fields.StringField()
    count = fields.IntField()

class Prices(Document):
    max_price = fields.FloatField()
    min_price = fields.FloatField()
    avg_price = fields.FloatField()

class Charts(Document):
    count = fields.IntField()
    price = fields.FloatField()
    time = fields.StringField()

