import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)


class Basket:
    def __init__(self, bd):
        self.connection = sqlite3.connect(bd)
        self.cursor = self.connection.cursor()
        self.all_info = {}
        self.count = 0
        self.info()
        self.in_total = 0
        self.connection.close()

    def info(self):
        info = self.cursor.execute("""SELECT id, name_of_product, manufacturer, number_of_items, cost_of_item,
                                        image FROM items""").fetchall()
        for item in info:
            self.all_info[item[0]] = item[1:]
        self.add()

#  beautiful_soup find() find elements
    def add(self):
        pick_information = request.form.get('')  # выявление какой продукт был выбран
        for k, v in self.all_info.items():
            if k == pick_information:
                self.count += 1
                self.in_total += pick_information['price']
                self.cursor.execute(f"""INSERT INTO basket(id,name_of_product,manufacturer,number_of_items,
                cost_of_item,image,total_sum,quantity) VALUES({k,v[0],v[1],v[2],v[3],v[4],self.in_total,self.count})""")

    def delete(self):
        product_delete = request.form.get('')  # выявление какой продукт мы хотим удалить с корзины
        for k, v in self.all_info.items():
            if k == product_delete:
                self.cursor.execute(f"""DELETE from basket WHERE id == {k}""")


mini_basket = Basket('name.db')

