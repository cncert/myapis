from flask import render_template,redirect,jsonify
import json
import requests
from flask.views import MethodView
from apis import people_blu

#5f4253c3b3de4041973702999f7e5f2c
# 635870838@qq.com  w635870838


class Weather(MethodView):
    def get_data(self,city_id):
        payload = {'city':city_id,'key':'5f4253c3b3de4041973702999f7e5f2c'}
        request_data = {}
        data = requests.get('https://free-api.heweather.com/v5/now', params=payload)
        data = data.json()
        basic = data["HeWeather5"][0]["basic"]
        now = data["HeWeather5"][0]["now"]
        city = basic["city"]  # 城市
        update_time = basic["update"]["loc"]  # 更新时间
        cond = now["cond"]["txt"]  # 天气状况
        tmp = now["fl"]  # 体感温度
        hum = now["hum"]  # 湿度
        pcpn = now["pcpn"]  # 降水量
        wind_dir = now["wind"]["dir"]  # 风向
        wind_sc = now["wind"]["sc"]  # 风力
        wind_spd = now["wind"]["spd"]  # 风速

        request_data['城市'] = city
        request_data['天气状况'] = cond
        request_data['温度'] = tmp
        request_data['湿度'] = hum
        request_data['降水量'] = pcpn
        request_data['风向'] = wind_dir
        request_data['风力'] = wind_sc
        request_data['风速'] = wind_spd + ' km/小时'
        request_data['更新时间'] = update_time
        return request_data

    def get(self, city_id):
        if city_id is None:
            # return a list of weather
            city_id = 'beijing'
            request_data = self.get_data(city_id)
            return json.dumps(request_data,ensure_ascii=False,indent=2)
        else:
            # expose a single weather
            try:
                request_data = self.get_data(city_id)
            except:
                city_id = 'beijing'
                request_data = self.get_data(city_id)
            return json.dumps(request_data,ensure_ascii=False,indent=2)

    def post(self):
        # create a new user
        pass

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass

@people_blu.route('/index')
def index():
    data = {
        'data':'yes'
    }
    return jsonify(data)


