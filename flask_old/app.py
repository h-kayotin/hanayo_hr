#encoding:utf-8
from flask import Flask
from flask import render_template
import _thread,time

from flask import request
from servers.data import main
from servers import xinzi,xueli,jinyan
from flask_sqlalchemy import SQLAlchemy#导入SQLAlchemy模块，连接数据库
from sqlalchemy import or_
import config#导入配置文件

app = Flask(__name__)#Flask初始化

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.from_object(config)#初始化配置文件
db = SQLAlchemy(app)#获取配置参数，将和数据库相关的配置加载到SQLAlchemy对象中



from models.models import Data    #导入user模块
#创建表和字段


@app.route('/')
def first():
    return render_template("input.html")

@app.route('/list')#定义路由
def list():#定义hello_world函数
    # data = Data.query.all()
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 2))
    key = request.args.get('key', '')
    # Data.address.like("%{}%".format('java'))
    data = Data.query.filter(or_(Data.post.like("%{}%".format(key)),
                                 Data.company.like("%{}%".format(key)),
                                 Data.address.like("%{}%".format(key)),
                                 Data.salary_max.like("{}".format(key)),
                                 Data.salary_min.like("{}".format(key)) )).paginate(page, 12, error_out=False)
    return render_template("data.html", datas=data,key=key)


@app.route('/search')
def search():
    kw =request.args.get("kw")
    city =request.args.get("city")

    # main(kw, city)
    # 创建两个线程
    try:
        _thread.start_new_thread(main, (kw, city, 1,))
        _thread.start_new_thread(main, (kw, city, 51,))
    except:
        print("Error: 无法启动线程")

    time.sleep(50)
    xz = xinzi.xinzi()
    xl = xueli.xuelifun()
    jy = jinyan.jinyanfun()
    return render_template('h.html', **locals())


#通过url传递信息
@app.route('/chart')
def charts():
    xz =xinzi.xinzi()
    xl = xueli.xuelifun()
    jy = jinyan.jinyanfun()
    return render_template('h.html',**locals())


#通过url传递信息
@app.route('/xinzi')
def xinzitest():
    a = xinzi.xinzi()
    print(a)
    return str(a)

@app.route('/xueli')
def xuelitest():
    data = xueli.xuelifun()
    print(data)

    return str(data)

if __name__ == '__main__':
    app.run()




