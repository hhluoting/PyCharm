from flask import Flask, render_template, request
import pymysql

# 初始化Flask应用
app = Flask(__name__)
# 配置MySQL连接参数
app.config['MYSQL_DATABASE_USER'] = 'python'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Y277stNbyeJS2hkN'
app.config['MYSQL_DATABASE_DB'] = 'python'
app.config['MYSQL_DATABASE_HOST'] = '192.168.40.241'

# 创建连接
mysql = pymysql.connect


# 路由和视图函数
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取表单数据
        username = request.form['username']
        age = request.form['age']
        # 根据条件查询数据库
        query = "SELECT * FROM users"
        if username:
            query += " WHERE username LIKE %s"
        if age:
            if username:
                query += " AND"
            query += " age = %s"

        # 执行查询
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query, (f"%{username}%", age) if username else (age,))
        users = cursor.fetchall()
        cursor.close()

        # 渲染查询结果
        return render_template('index.html', users=users)
    else:
        # 渲染初始页面
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
