import requests
from lxml import html
from lxml import etree
session_requests = requests.session()

login_url = "http://mydy.dypatil.edu/rait/login/index.php?uname=san.yad.rt15@rait.ac.in&wantsurl="
result = session_requests.get(login_url)
form_data = {
    "uname_static": "san.yad.rt15@rait.ac.in",
    "username": "san.yad.rt15@rait.ac.in",
    "uname": "san.yad.rt15@rait.ac.in",
    "password": "dypatil@123"
}

result0 = session_requests.post(
    login_url,
    data=form_data,
    headers=dict(referer=login_url)
)
url = "http://mydy.dypatil.edu/rait/my/"
result1 = session_requests.get(
    url,
    headers = {"Cache-Control": "no-store, no-cache, must-revalidate, post-check=0, pre-check=0",
    "Connection": "Keep-Alive",
    "Content-Language": "en",
    "Content-Length": "427",
    "Content-Type": "text/html; charset=utf-8",
    "Keep-Alive": "timeout=5, max=98",
    "Location": "http://mydy.dypatil.edu/rait/",
    "Pragma": "no-cache",
    "Server": "Apache/2.4.6 (CentOS) PHP/5.4.16",
    "X-Powered-By": "PHP/5.4.16"}
)
tree = html.fromstring(result.content)
# print(html.tostring(tree))
subjects = tree.xpath('//*[@class="launchbutton"]/@href')

# for subject in subjects:
#     print(subject)

for elem in tree.xpath('//*[@class="launchbutton"]'):
     print(etree.tostring(elem, pretty_print=True))