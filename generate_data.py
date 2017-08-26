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
    max_sales_number = 10000
    start_dt = "2014-01-01 00:00:00"

    

    for goods_id in xrange(max_goods_number*0, max_goods_number*1):

        # 价格
        # 随机生成，20-30次变一次
        max_price_times = random.randint(20, 30)
        current_price_times = 0
        current_price = float('%.2f' % random.uniform(100, 150))

        # time
        sold_time = datetime.datetime.strptime(start_dt, "%Y-%m-%d %H:%M:%S")

        for sales_count in xrange(max_sales_number):

            # 计算商品售出时间，随机递增
            seconds = random.randint(1000, 2000)
            sold_time = sold_time + datetime.timedelta(seconds = seconds)
            
            # 商品售出价格
            if current_price_times >= max_price_times:
                max_price_times = random.randint(20, 30)
                current_price_times = 0
                current_price = float('%.2f' % random.uniform(100, 150))

            current_price_times = current_price_times + 1

            # 写入数据库
            good_sales_record = {'goods_id': goods_id,
                                 'sold_time': sold_time, 'sold_price': current_price}
            print good_sales_record
            # collection.save(good_sales_record)
            db.goods_sales.insert(good_sales_record)

    end_time = datetime.datetime.now()
    print end_time - start_time

if __name__ == '__main__':
    insert_data()
