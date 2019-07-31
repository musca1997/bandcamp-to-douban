# bandcamp-to-douban
从bandcamp爬取专辑信息、封面图并上传豆瓣条目的自动化小工具


# requirements
python3.6
requests
bs4

# how to run 使用指南
编辑文本，将自己账号的cookies和ck填入（在chrome环境下f12可以找到）

运行脚本 `python bc2douban.py`

按照要求填入bandcamp的专辑url

选择豆瓣对应的专辑分类

![](https://cdn.discordapp.com/attachments/447635828496138241/606172280300634112/sample2.PNG)

脚本运行界面

![](https://cdn.discordapp.com/attachments/447635828496138241/606172270913912915/sample1.PNG)

条目上传成功界面（支持封面上传）

# 使用须知
因个人喜好，为了方便所以直接把介质默认设置成了数字（Digital）

专辑类型默认为专辑



# to do
有精力可以写个图形界面

或者有精力的网友fork一下写个图形界面版的
