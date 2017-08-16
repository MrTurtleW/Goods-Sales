# -*- coding:utf-8 -*-

from pymongo import MongoClient
import random
import time
import datetime


def insert_data():

    start_time = datetime.datetime.now()

    client = MongoClient()
    db = client['goods']
    collection = db['goods_sales']

    max_goods_number = 1000
    max_sales_number = 1000
    start_dt = "2014-01-01 00:00:00"

    timeArray = time.strptime(start_dt, '%Y-%m-%d %H:%M:%S')
    start_timestamp = time.mktime(timeArray)

    for goods_id in xrange(max_goods_number):

        # 价格
        # 随机生成，20-30次变一次
        max_price_times = random.randint(20, 30)
        current_price_times = 0
        current_price = float('%.2f' % random.uniform(100, 150))

        # 日期
        current_timestamp = start_timestamp

        for sales_count in xrange(max_sales_number):

            # 计算商品售出时间，0-10秒随机递增
            current_timestamp += random.randint(0, 10)
            sold_time = datetime.datetime.fromtimestamp(current_timestamp)
            print sold_time
            # 商品售出价格
            if current_price_times >= max_price_times:
                max_price_times = random.randint(20, 30)
                current_price_times = 0
                current_price = float('%.2f' % random.uniform(100, 150))
                print current_price

            current_price_times = current_price_times + 1

            # 写入数据库
            good_sales_record = {'goods_id': goods_id,
                                 'sold_times': sold_time, 'sold_price': current_price}
            print good_sales_record
            collection.save(good_sales_record)

    end_time = datetime.datetime.now()
    print (end_time - start_time).seconds

if __name__ == '__main__':
    insert_data()
