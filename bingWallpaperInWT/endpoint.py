import requests
import json
import os
import io

URL = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx={cur}&n=1&mkt=zh-CN'
BASE_URL = 'https://cn.bing.com'
SUFFIX = '_UHD.jpg'


# https://www.cnblogs.com/soupig/p/9981397.html
def get_single_image_url(index):
    r = requests.get(URL.format(cur=index))
    response = json.loads(r.content.decode(encoding='utf-8'))
    if (not response) or (not response['images']) or (not response['images'][0]) or (
            not response['images'][0]['urlbase']):
        return None
    return BASE_URL + response['images'][0]['urlbase'] + SUFFIX


def get_single_image(img_url, img_path):
    r = requests.get(img_url)
    with open(img_path, 'wb') as f:
        f.write(r.content)


def get_single_image_stream(img_url):
    image_bytes = requests.get(img_url).content
    data_stream = io.BytesIO(image_bytes)
    return data_stream


def change_windows_terminal_background(config_path, img_path):
    with open(config_path, 'r+') as f:
        config_data = json.load(f)
        if not config_data or not config_data['profiles'] or not config_data['profiles']['list']:
            return
        for data in config_data['profiles']['list']:
            if 'backgroundImage' in data:
                data['backgroundImage'] = img_path
        f.seek(0)
        f.truncate()
        f.write(json.dumps(config_data, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    url = get_single_image_url(0)
    path = os.path.join('D:\\', 'BingWallpaper', 'test.jpg')
    get_single_image(url, path)
    c_path = b'C'
    print(c_path)
    change_windows_terminal_background(c_path, path)
