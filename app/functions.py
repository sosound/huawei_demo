import os
import logging
import traceback
import json
import requests


def robot_push(url, mes_content):
    """
    :param url: 企微机器人url
    :param mes_content: 需要推送的信息
    :return: 推送情况
    """
    result = {
        "code": 0,
        "message": "",
        "data": {},
        "real_message": "",
    }
    mes = {
        "msgtype": "markdown",
        "markdown": {
            # "title": mes_title,
            "content": mes_content,
        },
    }
    headers = {
        'Content-Type': 'application/json',
    }
    try:
        response = requests.post(url, data=json.dumps(mes), headers=headers)
        logging.info(f'企微群消息机器人返回：{response.text}')
        result["data"] = response.text
    except BaseException as e:
        # error_message = traceback.format_exc()
        # logging.error(f'error:{e}\n{error_message}')
        result["code"] = -1
        result["message"] = "wecom robot api error"
        # result["real_message"] = error_message
    return result
