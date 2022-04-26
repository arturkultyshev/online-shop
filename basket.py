import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)


class Basket:
    def __init__(self, bd):
        self.connection = sqlite3.connect(bd)
        self.cursor = self.connection.cursor()
        self.all_info = None
        self.count = {}
        self.info()
        self.in_total = 0
        self.connection.close()

    def info(self):
        self.all_info = self.cursor.execute("""SELECT info FROM tab""").fetchall()
        self.add()

    def add(self):
        pick_information = request.form.get('')
        for i in self.all_info:
            if i == pick_information:
                self.count[pick_information['id']] = 1
                self.in_total += pick_information['price']
                self.cursor.execute("""INSERT INTO something(count) VALUES(something, 1)""")
            else:
                self.count[pick_information['id']] = self.count.get([pick_information['if']]) + 1
                self.in_total += pick_information['price']
                self.cursor.execute(f"""INSERT INTO tab(count) VALUES({self.count[pick_information['id']]}""")

    def delete(self):
        self.cursor.execute("""DELETE from tab FILTER""")


mini_basket = Basket('name.db')

