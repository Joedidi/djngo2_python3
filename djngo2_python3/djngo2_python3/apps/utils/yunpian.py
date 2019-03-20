# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     yunpian
   Description :
   Author :       jusk?
   date：          2019/3/19
-------------------------------------------------
   Change Activity:
                   2019/3/19:
-------------------------------------------------
"""

import requests
import json

class YumPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        # 需要传递的参数
        parmas = {
            "apikey":self.api_key,
            "mobile":mobile,
            "text":"【杭州立幼网】你的验证码是{code}。如非本人操作，请忽略本短信".format(code=code),
        }
        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict
if __name__=="__main__":
    yum_pian = YumPian("xxxx")
    yum_pian.send_sms("2018", "手机号码")