from flask import Flask,request,jsonify
#
# from flask_httpauth import HTTPDigestAuth
# from werkzeug.security import generate_password_hash, check_password_hash

from human import Human
import requests
import datetime
app = Flask(__name__)
import logging
logging.basicConfig(filename='connectHikFaceNX.log', level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
app.config['SECRET_KEY'] = 'trertertefdx4523$@2`'
#
# auth = HTTPDigestAuth()
# users = {
#     "qwe": "ewq1"
# }
#
# @auth.get_password
# def get_pw(username):
#     if username in users:
#         return users.get(username)
#     return None

@app.route('/', methods=['GET', 'POST'])
def defo():
    data = request.data
    #alarmResult = request.args.get('ipAddress')
    print(data)
    logging.info(" remote_ip : {}, route =  '/'".format(request.remote_addr))
    print("=============")
    return 'hello'

'''
@app.route('/test',methods=['GET', 'POST'])
def test():
    data = request.data

    #alarmResult = request.args.get('ipAddress')
    print(alarmResult)

    return 'jkh'
'''

@app.route('/alarm',methods=['GET', 'POST'])
def hello():
    data = request.get_json()
    # contents = urllib.request.urlopen("http://example.com/foo/bar").read()
    # logging.info(" remote_ip : {}, route =  '/alarm'".format(request.remote_addr))
    # logging.info(" route =  '/alarm', response : {} ".format(data))
    print("/alarm, response : {}, time : {}".format(data, datetime.datetime.now()))
    return 'alarm'


@app.route('/motion_alarm', methods=['GET', 'POST'])
def motion_alarm():
    data = request.get_json()
    # logging.info(" remote_ip : {}, route =  '/alarm'".format(request.remote_addr))
    # logging.info(" route =  '/alarm', response : {} ".format(data))
    print("/motion_alarm, response : {}, time : {}".format(data, datetime.datetime.now()))
    return 'motion_alarm'




@app.route('/http_alarm', methods=['GET', 'POST'])
# @auth.login_required
def http_alarm():
    data = request.get_json()
    # logging.info(" remote_ip : {}, route =  '/alarm'".format(request.remote_addr))
    # logging.info(" route =  '/alarm', response : {} ".format(data))
    print("/http_alarm, response : {}, time : {}".format(data, datetime.datetime.now()))
    print("/, response.content(request) : {}, time : {}".format(request.headers, datetime.datetime.now()))
    print("/, response.content(request) : {}, time : {}".format(request.data, datetime.datetime.now()))
    print("===================")
    return 'http_alarm'

@app.route('/lpr_camera', methods=['GET', 'POST'])
# @auth.login_required
def lpr_camera():
    data = request.get_json()
    print("HEADERS", request.headers)
    print("REQ_path", request.path)
    print("ARGS", request.args)
    print("DATA", request.data)
    print("FORM", request.form)

    # logging.info(" remote_ip : {}, route =  '/alarm'".format(request.remote_addr))
    # logging.info(" route =  '/alarm', response : {} ".format(data))
    print("/lpr_camera, response : {}, time : {}".format(data, datetime.datetime.now()))
    print("/, response.content(request) : {}, time : {}".format(request.headers, datetime.datetime.now()))
    print("/, response.content(request) : {}, time : {}".format(request, datetime.datetime.now()))

    # with open("C:\\Users\\User\\PycharmProjects\\FCFlask\\photos", 'wb') as f:
    #     for chunk in request:
    #         f.write(chunk)
    # img_data = requests.get(image_url).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(request.data)
    print("===================")
    return 'lpr_camera'


if __name__ == '__main__':
    app.run(host="192.168.30.130", port=5000,
            threaded=True)
