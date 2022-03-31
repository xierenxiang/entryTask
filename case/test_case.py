# pytest测试框架管理测试用例  pip install requests, pip install pytest,pyyaml
import json
import os

import allure
import pytest
import requests
from Load_data import yaml_load


@allure.feature('InterFace')
@allure.epic('Entrytask')
@allure.story('Basic')
@pytest.mark.parametrize('data', yaml_load.load('../Data/data.yaml'))
def test_01(data):
    # 测试url
    url = 'http://127.0.0.1:8080/test_v1'

    res = requests.get(url, params=data['case'])
    print(res.text)

    resjson = json.loads(res.text)
    reference = data['reference']
    msg = data['error_message']

    assert msg == resjson['error_message']
    assert reference == resjson['reference']


@allure.feature('InterFace')
@allure.epic('Entrytask')
@allure.story('Basic')
@pytest.mark.parametrize('data', yaml_load.load('../Data/dataException.yaml'))
def test_02(data):
    # 测试url
    url = 'http://127.0.0.1:8080/test_v1'

    res = requests.get(url, params=data['case'])
    print(res.text)

    resjson = json.loads(res.text)
    msg = data['error_message']
    code = data['error_code']

    assert msg == resjson['error_message']
    assert code == resjson['error_code']


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/html'])
    os.system('pytest - -alluredir. / result')
    os.system('allure generate. / result / -o. / report / --clean')

    # 命令行生成测试报告

    # 1、生成测试报告数据
    # pytest - -alluredir =./ allure - xml
    #
    # 2、测试报告在线预览
    # allure
    # serve. / allure - xml
    #
    # 3、测试报告本地静态数据生成
    # allure
    # generate. / allure - xml - o. / allure - result --clean
