from django.shortcuts import render
from django.conf import settings
from categories.models import Category
from products.models import *
from decimal import Decimal, DecimalException
import os
import csv
import json
# main_categories=["Clothing","Women's Clothing"]
def do_laod_data(request):
    data=os.path.join(settings.BASE_DIR,"public/data_set/flipkart_com-ecommerce_sample.csv")
    with open(data) as file:
        reader = csv.reader(file,delimiter = ',')
        header = []
        data   = []
        categories = []
        iterator=0
        for row in reader:
            header = row
            break
        for row in reader:
            extracted_categories=row[4].replace("[","").replace("]","").replace(" ' ","").replace('"',"").split(">>")
            categories_strip=[extracted_categories[i].strip()  for i in  range(len(extracted_categories))][:-1]
            if(len(categories_strip) == 0 ):
                continue
            main_category=categories_strip[0]
            del categories_strip[0]
            try:
                main_cate=Category.objects.get(name=main_category,is_parent=1)
            except Category.DoesNotExist:
                main_cate=Category(name=main_category,is_parent=1,parent_id=0)
                main_cate.save()
            category_id=main_cate.id
            for cat in categories_strip:
                try:
                    main_cate=Category.objects.get(name=cat,is_parent=0,parent_id=category_id)
                    category_id=main_cate.id
                except Category.DoesNotExist:
                    main_cate=Category(name=cat,is_parent=0,parent_id=category_id)
                    main_cate.save()
                    category_id=main_cate.id
            uniq_id = row[0]
            product_url = row[2]
            product_name = row[3]
            pid = row[5]
            retail_price = price_validation(row[6])
            discounted_price = price_validation(row[7])
            is_FK_Advantage_product =row[9][0].upper() + row[9][1:] #row[9]
            description =row[10]
            product_rating = price_validation(row[11])
            overall_rating = price_validation(row[12])
            brand=row[13]
            product_specifications = row[14]
            product_images = row[8]
            product_images_obj = product_images.replace("[","").replace("]","").replace("'","").replace('"',"").replace(" ","").split(",")
            product_specifications = product_specifications.replace("=>",":")
            product=Product(
                uniq_id=uniq_id,
                product_name=product_name,
                category_id=category_id,
                product_url=product_url,
                pid=pid,
                retail_price=retail_price,
                discounted_price=discounted_price,
                is_FK_Advantage_product=is_FK_Advantage_product,
                description=description,
                product_rating=product_rating,
                overall_rating=overall_rating,
                brand=brand
                )
            product.save()
            if(len(product_specifications)>0):
                json_object = json.loads(product_specifications)
                if type(json_object["product_specification"]) is list :
                    product_specifications=json_object["product_specification"]
                else:
                    product_specifications=[json_object["product_specification"]]
                make_specifications_product(product,product_specifications)
            make_images_products(product,product_images_obj)
    return
def price_validation(money):
    money_valid=0
    try:
        money_valid = Decimal(money)
    except DecimalException:
        money_valid = 0.0
    return money_valid
def make_images_products(product,images):
    for i in images:
       product_images= Product_images(product=product,image_url=i)
       product_images.save()
    pass
def make_specifications_product(product,specifications):
    # Product_specifications()
    for i in specifications:
        key=""
        value=""
        if "key" in i:
            key=i["key"]
        if "value" in i:
            value=i["value"]
        product_specifications=Product_specifications(product=product,key=key,value=value)
        product_specifications.save()
    pass