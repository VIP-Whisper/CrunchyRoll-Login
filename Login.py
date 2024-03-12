import requests
import uuid
from random import choice
from getuseragent import UserAgent
id = str(uuid.uuid4())
ua = UserAgent("ios").Random()
email='email'
psw='password'
response = requests.post("https://beta-api.crunchyroll.com/auth/v1/token", data={"username":email,"password":psw,"grant_type": "password","scope": "offline_access","device_id": id}, headers={"Etp-Anonymous-Id": id,"Content-Type": "application/x-www-form-urlencoded; charset=utf-8","Accept": "*/*","Authorization": "Basic cW1idnFfdXFuMmc2MXFrZm1vMHU6UkUyRERRMXJtdmQ4Y0dDUGphWHQxSk9aVk5FRTFCb0o=","Accept-Encoding": "gzip, deflate, br","User-Agent": ua,"Accept-Language": "ar-LY;q=1.0, en-GB;q=0.9","Connection": "close"})
if '"access_token"' in response.text:
    tk = response.json()['access_token']
    user_info_response = requests.get("https://beta-api.crunchyroll.com/accounts/v1/me", headers={"Host": "beta-api.crunchyroll.com","Authorization": f"Bearer {tk}","Accept-Encoding": "gzip, deflate, br","User-Agent": "Crunchyroll/3.45.4 Android/9 okhttp/4.12.0"})
    external_id = user_info_response.json()['external_id']
    subscription_info_response = requests.get(f"https://beta-api.crunchyroll.com/subs/v1/subscriptions/{external_id}/benefits", headers={"Host": "beta-api.crunchyroll.com","Authorization": f"Bearer {tk}","Accept-Encoding": "gzip, deflate, br","User-Agent": "Crunchyroll/3.45.4 Android/9 okhttp/4.12.0"})
    if 'fan' in str(subscription_info_response.json()):
     print('Fan')
    elif 'premium' in str(subscription_info_response.json()):
     print('Premium')
    elif 'Subscription Not Found' in str(subscription_info_response.json()):
     print('Free')
elif 'invalid_credentials' in response.text:
     print("Login failed: Invalid credentials")