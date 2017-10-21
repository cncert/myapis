# 将视图函数添加到路由系统

from apis import people_blu
# endpoint是断点，比如： endpoint='weather',那么url必须等于='/weather/'（最后加斜杠'/'）


def register_api(bluprint,view, endpoint, url, pk='id'):
    view_func = view.as_view(endpoint)
    bluprint.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    bluprint.add_url_rule(url, view_func=view_func, methods=['POST',])
    bluprint.add_url_rule('%s<%s>' % (url, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])
    # 第3个url适用于： http://127.0.0.1:5000/people/weather/2