# -*-coding:utf-8-*-

from flask import Flask, request
import json
import logging
# from flask_apispec import use_kwargs, marshal_with
# from marshmallow import fields
import datetime
from Flask_test.errenum import ErrorCode

# 1.创建flask实例
app = Flask(__name__)


# 当b不为空时，reference返回具体数据

# 只接受get方法访问
# 路由地址传参类型默认为字符串
@app.route("/test_v1", methods=["GET"])
def check():
    # 请求开始时间
    starttime = datetime.datetime.now()

    # 默认返回内容
    return_dict = {'error_code': ErrorCode.SUCCESS_CODE, 'error_message': 'success', 'reference': False}

    # logging.info('请求开始' + '-' * 20)
    # 判断入参是否为空
    if request.args is None:
        return_dict['error_code'] = ErrorCode.SYSTEM_ERRCODE
        return_dict['error_message'] = 'system error'
        return json.dumps(return_dict, ensure_ascii=False)

    # 获取传入的params参数
    get_data = request.args.to_dict()
    a_value = get_data.get('a')
    b_value = get_data.get('b')

    # 判断a,b是否为空
    if a_value is None and b_value is None:
        return_dict['error_code'] = ErrorCode.SYSTEM_ERRCODE
        return_dict['error_message'] = 'system error'
        return json.dumps(return_dict, ensure_ascii=False)

    # 判断a的值是否为整形
    if a_value is not None:
        if not a_value.isdigit():
            return_dict['error_code'] = ErrorCode.PARAMS_ERRCODE
            return_dict['error_message'] = 'param:a must be positive int'

            endtime = datetime.datetime.now()
            print((endtime - starttime).microseconds / 1000)
            return json.dumps(return_dict, ensure_ascii=False)
        # elif valueRange(a_value):
        #     return_dict['error_code'] = ErrorCode.PARAMS_ERRCODE
        #     return_dict['error_message'] = 'param:a must in (0,100)'
        #     return json.dumps(return_dict, ensure_ascii=False)

    # b is the necessary data .
    if not b_value:
        return_dict['error_code'] = ErrorCode.PARAMS_ERRCODE
        return_dict['error_message'] = 'param :b is the necessary code.'
        endtime = datetime.datetime.now()
        print((endtime - starttime).microseconds / 1000)
        return json.dumps(return_dict, ensure_ascii=False)

    # b不可以为空
    if len(b_value) == 0 or b_value == '':
        return_dict['error_code'] = ErrorCode.PARAMS_ERRCODE
        return_dict['error_message'] = 'b can not be empty.'
        endtime = datetime.datetime.now()
        print((endtime - starttime).microseconds / 1000)
        return json.dumps(return_dict, ensure_ascii=False)

    # 对返回参数进行操作
    # 去除参数前置携带的多余空格后返回
    if a_value is None:
        return_dict['reference'] = 'b:' + b_value.lstrip()
    else:
        return_dict['reference'] = tt(a_value.lstrip(), b_value.lstrip())

    endtime = datetime.datetime.now()
    print((endtime - starttime).microseconds / 1000)
    return json.dumps(return_dict, ensure_ascii=False)


# # 只接受POST方法访问
# @app.route("/test_v2", methods=["POST"])
# def check():
#     # 默认返回内容
#     return_dict = {'error_code': '200', 'error_message': 'success code', 'reference': False}
#     # 判断入参是否为空
#     if request.args is None:
#         return_dict['error_code'] = '5004'
#         return_dict['error_message'] = 'param :b is the necessary code.'
#         return json.dumps(return_dict, ensure_ascii=False)
#     # 获取传入的params参数
#     get_Data= json.loads(request.get_data())
#
#     name = get_Data.get('a')
#     age = get_Data.get('b')
#     # 对参数进行操作
#     return_dict['result'] = tt(name, age)
#
#     return json.dumps(return_dict, ensure_ascii=False)

# 功能函数
def tt(a, b):
    result_str = "a:%s,b:%s" % (a, b)
    return result_str


# 判断值在规定范围内
def valueRange(a):
    if a in range(0, 100000):
        return True
    else:
        return False


if __name__ == "__main__":
    # 2.运行run方法
    app.run('localhost', 8080)
