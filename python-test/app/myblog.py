import time
from  flask import  Flask,Markup,url_for,render_template,request,redirect,session,make_response,abort
import testMysql
from datetime import timedelta,datetime 
from exception_define import InvalidUsage
from logging.handlers import TimedRotatingFileHandler
import logging,os

app  =  Flask(__name__)
app.secret_key = 'i am so cute'
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=1)

@app.route('/')
def  indexUnLogin():
#     return  Markup('<div>Hello %s</div>')  %  '<em>Flask</em>'
    return redirect("https://www.baidu.com/")

@app.route('/hello')
@app.route('/hello/<name>')
def  hello(name=None):
    
    return  render_template('/hello.html', name=name)

@app.route('/test')
def  test(name=None):
    return  render_template('/test3.html')

@app.route('/directory')
def  directory():
    return  render_template('/directory.html')

def query_user(username):
    return testMysql.query(username)

@app.route('/user')
def  user():
#     return  render_template('/user.html',dataList=testMysql.query())
    return  render_template('/user.html',dataList=testMysql.batch_query())

@app.route('/htmlTest')
def  htmlTest():
#     return  render_template('/user.html',dataList=testMysql.query())
    return  render_template('/htmlTest.html')

@app.route('/notebook')
def  notebook():
#     return  render_template('/user.html',dataList=testMysql.query())
    return  render_template('/notebook.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    response=None
    local_time=time.strftime('%Y-%m-%d %H:%M:%S')
    session['welcome_str'] = 'you logged in on %s' %  local_time
    if request.method == 'POST':
        passwd=query_user(request.form['user'])[2]
        if passwd != None and request.form['password'] == passwd:
            session['user'] = request.form['user']
#             response=make_response(render_template('index.html',data=welcome_str,name=session['user']),200)
#             response.set_cookie('login_time',local_time)
            return redirect(url_for('index'))
        else:
            response=make_response(render_template('login.html',name=request.form['user'],prompt='Cause of login failure:Your passwd input error Or no such User!'),200)
            app.logger.error("login fail")
            return response
    else:
        if 'user' in session:
            login_time = request.cookies.get('login_time')
#             response=make_response(render_template('index.html', name=session['user'],data=welcome_str),200)
#             return response
            return redirect(url_for('index'))
        else:
            username = request.args.get('username', 'Sir Or Madam')
            response=make_response(render_template('login.html', name=username),200)
            response.headers['key']='value'
            app.logger.error("login fail")
            return response

@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('/index.html',data=session['welcome_str'],name=session['user'])

@app.route('/insert_web/', methods=['POST', 'GET'])
def  insert_web():
    return  render_template('/insert_web.html', title='HomePage')

@app.route('/insert_user', methods=['POST', 'GET'])
def insert_user():
    if request.method == 'POST' or request.method == 'GET':
        if request.form['name'] != None and request.form['age'] != None and request.form['passwd'] != None and request.form['address'] != None:
            data=[request.form['name'],request.form['age'],request.form['passwd'],request.form['address']]
            testMysql.insert(data)        
    return redirect(url_for('user'))

@app.route('/update/<username>', methods=['POST', 'GET'])
def  update_web(username):
    dataList=query_user(username)
    print(dataList)
    return  render_template('/update_web.html', data=dataList)

@app.route('/update_user', methods=['POST', 'GET'])
def update_user():
    if request.method == 'POST' or request.method == 'GET':
        if request.form['name'] != None and request.form['age'] != None and request.form['passwd'] != None and request.form['address'] != None:
            data=[request.form['age'],request.form['passwd'],request.form['address'],request.form['name']]
            testMysql.update(data)        
    return redirect(url_for('user'))

@app.route('/delete/<username>', methods=['POST', 'GET'])
def  delete_web(username):
    if username != None:
            testMysql.delete(username)
#     return  render_template('/delete_web.html', title='HomePage')
#     return render_template('login.html')
    return redirect(url_for('user'))

@app.route('/htmlWrite', methods=['POST', 'GET'])
def htmlWrite():
    with open("_result.html",'w') as f:
        data=request.form['html1']
        f.writelines(data)
        f.flush()

@app.route('/logout')
def logout():
    session.pop('user', None)   #delete session
    session.clear()             
    return redirect(url_for('login'))

@app.route('/error')
def error():
    abort(404)
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(InvalidUsage)
def invalid_usage(error):
    response = make_response(error.message)
    response.status_code = error.status_code
    print(response)
    return Markup.unescape('<h1 align="center">%s</h1>') % error.message
#     return response

@app.route('/exception')
def exception():
#     app.logger.debug('Enter exception method')
    app.logger.fatal('403 error happened')
    raise InvalidUsage('No privilege to access the resource',status_code=403)

def init_log():
    'init logging info'
    logfile = 'logs/{0}/my_log-{1}.log'.format(datetime.now().strftime("%Y%m"), datetime.now().strftime("%Y%m%d"))

    if not os.path.exists(os.path.dirname(logfile)):
        os.makedirs(os.path.dirname(logfile))

    server_log = TimedRotatingFileHandler(logfile,'D')
    server_log.setLevel(logging.INFO)
    server_log.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    
    app.logger.addHandler(server_log)

if  __name__  ==  '__main__':
    init_log()
    
    app.run(host='0.0.0.0', debug=True)
    
    