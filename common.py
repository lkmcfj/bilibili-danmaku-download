import time
import requests

FORBID = r'<>:"/\|?*'
REPLACE = '_'
def escape_filename(s):
    for ch in FORBID:
        s = s.replace(ch, REPLACE)
    return s.strip()

def comments_url(cid):
    return f'https://comment.bilibili.com/{cid}.xml'

DELAY = 0.5
def download(url_list, filename_list):
    headers = {}
    headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    headers['accept'] = '*/*'
    headers['accept-language'] = 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7'
    sess = requests.Session()
    sess.headers.update(headers)
    for url, filename in zip(url_list, filename_list):
        time.sleep(DELAY)
        res = sess.get(url)
        assert res.ok
        assert res.status_code == 200
        with open(filename, 'wb') as f:
            f.write(res.content)