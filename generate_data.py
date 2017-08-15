# -*- coding:utf-8 -*-

from pymongo import MongoClient
import random
import time

def insert_data():
    client = MongoClient()
    db = client['test']
    collection = db['test']

    max_goods_number = 1000000
    start_dt = "2014-01-01 00:00:00"
    end_dt = "2015-03-01 00:00:00"
    start_timestamp = 0
    end_timestamp = 0

    timeArray = time.strptime(start_dt, '%Y-%m-%d %H:%M:%S')
    start_timestamp = time.mktime(timeArray)
    timeArray = time.strptime(end_dt, '%Y-%m-%d %H:%M:%S')
    end_timestamp = time.mktime(timeArray)
    current_timestamp = start_timestamp

    # time_local = time.localtime(timestamp)
    # dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    # print start_timestamp
    # print end_timestamp

    price_max_times = random.randint(20, 30)
    current_price_times = 0
    current_price = '%.2f' % random.uniform(100, 150)

    for i in xrange(max_goods_number):
        # 随机生成商品ID
        goods_id = random.randint(0, 1000)
        # 计算商品售出时间，0-10秒随机递增
        current_timestamp = current_timestamp + random.randint(0, 10)
        # time_local = time.localtime(current_timestamp)
        # sold_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        # print sold_time
        # 商品售出价格
        if current_price_times >= price_max_times:
            price_max_times = random.randint(20, 30)
            current_price_times = 0
            current_price = '%.2f' % random.uniform(100, 150)
            print current_price
    
        current_price_times = current_price_times + 1
        # print current_price_times
        # 写入数据库
        # good_sales_record = {'goods_id':goods_id, 'sold_time':sold_time, 'sold_price':current_price}
        good_sales_record = {'goods_id':goods_id, 'sold_timestamp':current_timestamp, 'sold_price':current_price}
        print good_sales_record
        collection.save(good_sales_record)

if __name__ == '__main__':
    insert_data()
