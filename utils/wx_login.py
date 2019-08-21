import json
import requests
import base64
from Crypto.Cipher import AES


class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)

        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)

        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)))

        if decrypted["watermark"]["appid"] != self.appId:
            raise Exception("Invalid Buffer")

        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]


def wxlogin(code, encryptedData, iv, APPID, SECRET):
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code'.format(
        appid=APPID, secret=SECRET, code=code)
    response = requests.get(url=url)
    content = response.content.decode("utf-8")
    ret_dict = json.loads(content)
    pc = WXBizDataCrypt(APPID, ret_dict.get("session_key"))
    userinfo = pc.decrypt(encryptedData, iv)
    return userinfo


def get_oppenid(code, APPID, SECRET):
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code'.format(
        appid=APPID, secret=SECRET, code=code)
    try:
        response = requests.get(url=url)
        content = response.content.decode("utf-8")
        data = json.loads(content)
        return {'openid': data.get('openid'), 'session_key': data.get('session_key')}
        # return {'openid': data.get('openid')}
    except:
        return ""
