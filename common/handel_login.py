# coding=UTF-8
import requests
import json
import os
from common.handle_conf import conf

path = os.getcwd()+"\\"



# def login(key='test',value='url'):
#     login_url = "{}/cgi/easy-lead-personal-app/account-api/mobile-api/el-login".format(conf.get("env","base_url"))
#
#     data = {
#         'phone': conf.get("test_data","phone"),
#         'password': conf.get("test_data","password"),
#         'remember': 0,
#         'area_code': 86}
#     headers = {
#         'Referer':'{}/home'.format(conf.get("env","base_url"))
#     }
#
#     try:
#         r = requests.post(login_url,headers =headers, data=data)
#         x = r.cookies.get('accountCenterSessionId')
#         return x
#     except:
#         return "产生异常"

def login_company(key='test',value='url'):
    '''

    Parameters
    ----------
    company_id: 登录的企业id

    key: config.ini文件里面的【】，不用传值

    value: config.ini文件里面的值，不用传值

    Returns
    -------

    '''
    # x = login()

    # header = {
    #     'Referer':'https://user-test.tangees.com/home',
    #     'Cookie':'accountCenterSessionId='+ x
    #     }

    phone = conf.get("test_data","phone")
    pwd = conf.get("test_data","password")
    company_id = conf.get("test_data","company_id")
    data = {'phone' : phone,
            'password' : pwd,
            'company_id' : company_id,
            'login_type': 2,
            'app_version_type' : 1,
            'channel' : 'android',
            'app_version' : '2.0.3',
            'app_type' : 'easy_lead_app',
            'sign' : '83ab640fffb6334160bbfe5ba215751b'
            }

    r = requests.post(conf.get("env","base_url")+"/cgi/easy-lead-personal-app/account-api/mobile-api/el-login/select", data=data)

    print('登录成功！')

    # writeInfo = 'accountCenterSessionId='+ r.cookies.get("accountCenterSessionId")
    sessionid = r.json()['sessionId']
    # print(r.json())
    # print(sessionid)
    # print(writeInfo)
    return sessionid

Sessionid = login_company()
# cookies = login_company()
#print(cookies)

if __name__ == '__main__':
    # test_seconds = conf.get('test_num','num')
    # print(test_seconds)
    #login_company()
    print(Sessionid)