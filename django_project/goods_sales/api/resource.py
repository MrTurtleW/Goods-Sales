from tastypie.authorization import Authorization
from tastypie_mongoengine import resources
from tastypie.resources import ALL
from tastypie import fields
from datetime import datetime
from goods_sales.models import goods_sales


class ReturnObject(object):

    def __init__(self, initial=None):
        self.__dict__['_data'] = {}

        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def __getitem__(self, name):
        return self._data.get(name, None)

    def __setitem__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data


class MyModelResource(resources.MongoEngineResource):

    class Meta:
        queryset = goods_sales.objects.all()
        allowed_methods = ('get')
        excludes = ['id']
        authorization = Authorization()


class SalesResource(resources.MongoEngineResource):

    sold_month = fields.CharField(attribute='sold_month')
    count = fields.IntegerField(attribute='count')

    class Meta:
        allowed_methods = ('get')
        authorization = Authorization()
        resource_name = 'sales'
        excludes = ['resource_uri']

    def check_exist(self, lists, month):
        if len(lists) == 0:
            return

        for l in lists:
            if month == l['sold_month']:
                l['count'] = l['count'] + 1
                return True

        return False

    def get_object_list(self, request):
        try:
            if request.method == 'GET':
                self.gid = request.GET['goods_id']

        except:
            print 'parameter error'
            return

        queryset = goods_sales.objects(goods_id=self.gid)
        retList = []
        for q in queryset:
            sold_month = datetime.strftime(
                q.sold_time, "%Y-%m-%d %H:%M:%S")[0:7]
            if not self.check_exist(retList, sold_month):
                object = ReturnObject()
                object.sold_month = sold_month
                object.count = 1
                retList.append(object)

        return retList

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle.request)


class PricesResource(resources.MongoEngineResource):
    max_price = fields.FloatField(attribute='max_price')
    min_price = fields.FloatField(attribute='min_price')
    avg_price = fields.FloatField(attribute='avg_price')

    class Meta:
        allowed_methods = ('get')
        resource_name = 'prices'
        authorization = Authorization()

    def get_object_list(self, request):
        try:
            if request.method == 'GET':
                self.gid = request.GET['goods_id']
                self.timeStart = request.GET['timeStart']
                self.timeEnd = request.GET['timeEnd']

        except:
            print 'parameter error'
            return

        time_start = datetime.strptime(self.timeStart, '%Y-%m-%d %H:%M:%S')
        time_end = datetime.strptime(self.timeEnd, '%Y-%m-%d %H:%M:%S')

        queryset = goods_sales.objects(
            goods_id=self.gid, sold_time__gte=time_start, sold_time__lt=time_end)
        if queryset is None:
            return

        price = []
        retList = []
        for q in queryset:
            price.append(q.sold_price)

        object = ReturnObject()
        object.max_price = max(price)
        object.min_price = min(price)
        object.avg_price = sum(price) / len(price)

        retList.append(object)

        return retList

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle.request)


class ChartResource(resources.MongoEngineResource):
    count = fields.IntegerField(attribute='count')
    price = fields.FloatField(attribute='price')
    time = fields.CharField(attribute='time')

    class Meta:
        allowed_methods = ('get')
        resource_name = 'chart'
        authorization = Authorization()

    def get_object_list(self, request):
        try:
            if request.method == 'GET':
                self.gid = request.GET['goods_id']

        except:
            print 'parameter error'
            return

        queryset = goods_sales.objects(goods_id=self.gid)
        retList = []
        current_prices = []
        current_hour = ""
        current_count = 0

        for q in queryset:

            sold_hour = datetime.strftime(q.sold_time, "%Y-%m-%d %H:%M:%S")[0:13]

            if current_hour == "":
                current_hour = sold_hour
                current_count = 1
                current_prices.append(q.sold_price)

            elif current_hour == sold_hour:
                current_count = current_count + 1
                current_prices.append(q.sold_price)

            else:
                # print current_prices
                print sum(current_prices)

                object = ReturnObject()
                object.count = current_count
                object.time = current_hour + ":00:00"
                object.price = sum(current_prices) / current_count

                retList.append(object)
                current_hour = sold_hour
                current_count = 1
                current_prices = []
                current_prices.append(q.sold_price)

        return retList

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle.request)
