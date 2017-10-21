# apis/__init__.py, 本函数用于实例化蓝本,实例化后的蓝本既用于视图函数，又用于启动函数中app注册
# 请求---->run.py----->本函数----->视图函数

from flask import Blueprint

admin_blu = Blueprint('admin',__name__) # admin_blu、people_blu为实例化后的蓝本对象
people_blu = Blueprint('people',__name__) # 引号中的people是蓝图的名字，可以任意起

# 导入视图函数
from apis.admin import admin
from apis.people import people
from apis import register_api





