#将视图函数添加到路由系统

from apis.add_url import register_api
from apis import people_blu
from apis.people.people import Weather

#
register_api(people_blu,Weather,'weather','/weather/',pk='city_id')