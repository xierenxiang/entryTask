# coding=utf-8
import requests
from locust import HttpUser, TaskSet, task
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class MyTest(TaskSet):
    # 请求test_v1接口
    @task(1)
    def get_test(self):
        # 定义请求头
        # header = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

        req = self.client.get("/test_v1?a=100&b=bString")
        print(req.text)
        print('状态码为' + str(req.status_code))
        if req.status_code == 200:
            print("success")
        else:
            print("fails")


# 该类用于设置生成负载的基本属性
class TestV1(HttpUser):
    # 指向定义了用户行为的类
    tasks = [MyTest]
    # 模拟负载的任务之间执行时的最小等待时间，单位为毫秒
    min_wait = 1000  # 单位为毫秒
    max_wait = 6000  # 单位为毫秒


if __name__ == "__main__":
    import os

    os.system("locust -f case_excute.py --host=http://localhost:8080")
