from flask import Flask
from apis import admin_blu
from apis import people_blu

app = Flask(__name__)
app.register_blueprint(admin_blu,url_prefix='/admin')
app.register_blueprint(people_blu,url_prefix='/people')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
