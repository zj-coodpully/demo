from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index1.html')
@app.route('/zhuce')
def zhuce():
    return render_template('index.html')
#表单提交
@app.route('/login', methods=['GET','post'])
def login():
    username = request.form.get('username')
    print("name"+username)
    password = request.form.get('password')
    if username == '张运涛' and password == '123456':
        return render_template('index1.html', username=username,password=password)
    return render_template('login.html')

#表单提交
@app.route('/register', methods=['GET','post'])
def register():
    regname = request.form.get('regname')

    regpass = request.form.get('regpass')
    phone = request.form.get('phone')

    print("注册name" + regname+"\t"+regpass+"\t"+phone)
    import  pymysql


    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "pyzuoye", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句

    sql = "INSERT INTO user(username ,password,phone)VALUES ('" + regname +"','"+regpass+"','" + phone+"')"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # 关闭数据库连接
    db.close()
    return render_template('login.html')


@app.route('/')
def main():
    return render_template('login.html')

@app.route('/loginout')
def loginout():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('/home.html')
@app.route('/delete')
def delete():
    name = request.args.get('name')
    print("要删除的名字"+name)
    import pymysql

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "pyzuoye", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句

    sql = "delete from user where username ='"+name+"'"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # 关闭数据库连接
    db.close()
    return render_template('/delete.html')

@app.route('/updateedit')
def updateedit():
    name = request.args.get('name')
    print("要修改的名字"+name)
    import pymysql

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "pyzuoye", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句

    sql = "select * from user where username ='"+name+"'"
    try:
        # 执行sql语句
        cursor.execute(sql)
        myresult = cursor.fetchone()
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # 关闭数据库连接
    db.close()
    return render_template('/updateedit.html',myresult=myresult)
@app.route('/update', methods=['GET','post'])
def update():
    name = request.form.get('username')

    password = request.form.get('password')
    phone = request.form.get('phone')

    print("要修改的名字"+name)
    import pymysql

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "pyzuoye", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

    #sql = "update user set password = '"+password+"', phone= '"+phone+"' where username = '"+name+"'"
    sql = "update user set password = '" + password + "', phone= '" + phone + "' where username = '" + name + "'"
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        myresult = cursor.fetchone()
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # 关闭数据库连接
    db.close()
    return render_template('/update.html')

@app.route('/test')
def test():
    import pymysql

    db = pymysql.connect("localhost", "root", "root", "pyzuoye")

    cursor = db.cursor()

    sql = "select * from COLLEGE_INFO limit 100"

    cursor.execute(sql)

    myresult = cursor.fetchall()

    #for x in myresult:
        #print(x)

    db.close()

    return render_template("Sort_ads.html",schools=myresult)
@app.route('/userlist')
def userlist():
    import pymysql

    db = pymysql.connect("localhost", "root", "root", "pyzuoye")

    cursor = db.cursor()

    sql = "select * from user "

    cursor.execute(sql)

    myresult = cursor.fetchall()

    #for x in myresult:
        #print(x)

    db.close()

    return render_template("userlist.html",schools=myresult)
@app.route('/sdemo')
def sdemo():
    import pymysql

    db = pymysql.connect("localhost", "root", "root", "pyzuoye")

    cursor = db.cursor()

    sql = "select * from college_cutoff limit 500"

    cursor.execute(sql)

    myresult = cursor.fetchall()

    #for x in myresult:
        #print(x)

    db.close()

    return render_template("sdemo.html",schools=myresult)
if __name__ == '__main__':
    app.run()
