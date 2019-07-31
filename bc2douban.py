import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
"Referer": "https://music.douban.com/new_subject",
"Connection": "keep-alive",
#在此处填入你的账号cookies
"Cookie": '',
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Host": "music.douban.com",
"Origin": "https://music.douban.com/",
"Referer": "https://music.douban.com/new_subject"}
#在此处填入cookies里的ck
ck = ""


def submit():
    url = "https://music.douban.com/new_subject"
    data, image_link = fetch_bandcamp()
    data["p_116"] = genre()
    r = requests.post(data=data, url=url, headers=headers)
    soup = BeautifulSoup(r.content,"html.parser")
    nuid = soup.find("input", attrs={"name": "nuid"}).attrs['value']
    image_upload(nuid, image_link)


def image_upload(nuid, image_link):
    url = "https://music.douban.com/new_subject?nuid=" + nuid + "&update_image"
    files = {
        "ck": (None, ck),
        "nuid": (None, nuid),
        "picfile": ("cover.jpg", open("cover.jpg", "rb")),
        "img_submit": (None, "上传图片"),
        "as_new": (None, "t")
    }
    r = requests.post(headers=headers, files=files, url=url)
    print('条目上传成功！详见：{}'.format(url.replace("&update_image", "").replace("nuid=", "mine&nuid=")))

def fetch_bandcamp():
    url = input('请输入你要上传的条目的bandcamp地址：')
    print('------从bandcamp爬取信息中------')
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    info = soup.find("meta", attrs={"name": "title"}).attrs['content'].split(", by ")
    title = str(info[0])
    artist = str(info[1])
    publisher = soup.find("meta", attrs={"property": "og:site_name"}).attrs['content']
    date = soup.find("meta", attrs={"itemprop": "datePublished"}).attrs['content']
    desc = soup.find("meta", attrs={"name": "Description"}).attrs['content']
    date_list = list(date)
    date_list.insert(4, '-')
    date_list.insert(7, '-')
    date = ''.join(str(i) for i in date_list)

    image_link = soup.find("link", attrs={"rel": "image_src"}).attrs['href']
    img = requests.get(url=image_link)
    with open("cover.jpg", 'wb') as f:
        f.write(img.content)

    data = {
        "ck": ck,
        "p_27": title,
        "p_56": "",
        "p_48": "",
        "m_48": "",
        "p_48": "",
        "m_48": "",
        "p_48": artist,
        "m_48": "",
        "p_116": "",
        "p_57": "专辑",
        "p_49": "数字（Digital）",
        "p_50": publisher,
        "p_51": date,
        "p_55": "",
        "p_54": "",
        "p_52_other": "",
        "p_28_other": desc,
        "no_uid": "yes",
        "detail_subject_submit": "下一步",
        }
    print('信息爬取成功!')
    print(title)
    print(artist)
    print(publisher)
    print(date)
    print(desc)
    print('--------------------------------\n')

    return data, image_link

def genre():
    genres = ["Blues 布鲁斯",
    "Classical 古典",
    "Easy Listening 轻音乐",
    "Electronic 电子",
    "Folk 民谣",
    "Funk/Soul/R&B 放克/灵歌/R&B",
    "Jazz 爵士",
    "Latin 拉丁",
    "Pop 流行",
    "Rap 说唱",
    "Reggee 雷鬼",
    "Rock 摇滚",
    "Soundtrack 原声",
    "World 世界音乐"]
    for i in range(14):
        print(str(i+1) + ". " + genres[i])
    num = input('请选择音乐流派（输入对应的数字）')
    picked_genre = genres[int(num)-1]
    print('你选择了 -> {}, 上传条目中...'.format(picked_genre))
    return picked_genre


submit()
