import requests
import json
import configurator

# переменные для платформ dev/prod/rc
_BASE_URL = configurator.BASE_URL
_BASE_API_URL = configurator.BASE_API_URL

# путь post/get запроса


_PATH_USER = '/user/'
_PATH_PROFILE = '/browser/v2/'
_PATH_PROFILE_CREATE = '/browser/'

print(_BASE_URL)
print(_BASE_API_URL)


# запрос на авторизацию по api(используется в каждом тесте)
def get_user_info(token):
    url = _BASE_API_URL + _PATH_USER
    headers = {
        "Authorization": token,
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response


def get_profiles_info(token):
    url = _BASE_API_URL + _PATH_PROFILE
    headers = {
        "Authorization": token,
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response


def post_create_profile(token, name):
    url = _BASE_API_URL + _PATH_PROFILE_CREATE
    headers = {
        "Authorization": token,
        'Content-Type': 'application/json',
    }
    payload = {
        "name": name,
        "notes": name,
        "browserType": "chrome",
        "os": "lin",
        "startUrl": "string",
        "googleServicesEnabled": False,
        "lockEnabled": False,
        "debugMode": False,
        "navigator": {
            "userAgent": "string",
            "resolution": "string",
            "language": "string",
            "platform": "string",
            "doNotTrack": False,
            "hardwareConcurrency": 0,
            "deviceMemory": 1,
            "maxTouchPoints": 0
        },
        "geoProxyInfo": {},
        "storage": {
            "local": True,
            "extensions": True,
            "bookmarks": True,
            "history": True,
            "passwords": True,
            "session": True
        },
        "proxyEnabled": False,
        "proxy": {
            "mode": "http",
            "host": "string",
            "port": 0,
            "username": "string",
            "password": "string"
        },
        "dns": "string",
        "plugins": {
            "enableVulnerable": True,
            "enableFlash": True
        },
        "timezone": {
            "enabled": True,
            "fillBasedOnIp": True,
            "timezone": "string"
        },
        "audioContext": {
            "mode": "off",
            "noise": 0
        },
        "canvas": {
            "mode": "off",
            "noise": 0
        },
        "fonts": {
            "families": [
                "string"
            ],
            "enableMasking": True,
            "enableDomRect": True
        },
        "mediaDevices": {
            "videoInputs": 0,
            "audioInputs": 0,
            "audioOutputs": 0,
            "enableMasking": False
        },
        "webRTC": {
            "mode": "alerted",
            "enabled": True,
            "customize": True,
            "localIpMasking": False,
            "fillBasedOnIp": True,
            "publicIp": "string",
            "localIps": [
                "string"
            ]
        },
        "webGL": {
            "mode": "noise",
            "getClientRectsNoise": 0,
            "noise": 0
        },
        "clientRects": {
            "mode": "noise",
            "noise": 0
        },
        "webGLMetadata": {
            "mode": "mask",
            "vendor": "string",
            "renderer": "string"
        },
        "webglParams": [],
        "profile": "string",
        "googleClientId": "string",
        "updateExtensions": True,
        "chromeExtensions": [
            "string"
        ]}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response


def delete_profile(token, profile_id):
    url = _BASE_API_URL + _PATH_PROFILE_CREATE + profile_id
    headers = {
        "Authorization": token,
        'Content-Type': 'application/json',
    }
    payload = {"id": profile_id}

    response = requests.delete(url, headers=headers, data=json.dumps(payload))
    return response
