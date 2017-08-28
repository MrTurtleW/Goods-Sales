from mongoengine import Document
from mongoengine import fields

# Create your models here.


class goods_sales(Document):
    goods_id = fields.IntField()
    sold_time = fields.DateTimeField()
    sold_price = fields.DateTimeField()
