
from urllib import request, parse

with request.urlopen('https://www.baidu.com') as f:
    data = f.read()
    print ('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        #pass
        print ('%s: %s' % (k, v))
    print ('Data:', data.decode('utf-8'))


###########################################
print ('\n\n ############################## \n\n')

req = request.Request('http://www.douban.com')
req.add_header('User-Agent', 'Molilla/6.0 (iPhone: CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
#with request.urlopen(req) as f:
#    print ('Status:', f.status, f.reason)
#    for k, v in f.getheaders():
        #pass
#        print ('%s: %s', k, v)

#    print ('Data:', f.read().decode('utf-8'))


############################################

print ('\n\n ############################## \n\n')

print ('Login to weibo.cn...')
email = input('Email:')
passwd = input('Password:')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 Like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')


with request.urlopen(req, data = login_data.encode('utf-8')) as f:
    print ('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print ('%s: %s' % (k, v))
    print ('Data:', f.read().decode('utf-8'))
	
	
	
	
	
	
	
	

	
	
	
from enum import Enum, unique
from urllib import request, parse


# ======================================================
# Description:  程序调试相关设置
# Author:       linuxfor
# Email:        linuxfor@163.com
# ======================================================

has_debug = True             # 是否开启日志信息打印功能


def set_debug(flag):        # 开启日志打印
    global has_debug
    has_debug = flag


def reset_debug(flag):      # 关闭日志打印
    global has_debug
    has_debug = flag


def logd(*obj):             # 日志信息打印
    if has_debug is True:  # flag优先级比has_debug高
        print(*obj)

# ======================================================


# ======================================================
# 通过和风天气API，获取天气信息
# 产品计划：免费用户
# 有效期：永久
# 剩余每日按访问流量：3000次
# API请求参数：
# city      = 城市名称、支持中英文,不区分大小写和空格,城市和国家之间用英文逗号分割 (深圳、shenzhen、london,united kingdom)
# cityid    = 城市ID,参见 国内城市ID列表 (CN101280601)
# cityip    = 城市IP,输入所在城市的任意IP (123.45.67.8)
# key       = 用户认证key，需要注册才能获得
# ======================================================
class Weather(object):
    def __init__(self, city=''):
        self.__url_citylist = 'https://api.heweather.com/x3/citylist'
        self.__search = ['allchina', 'hotworld', 'allworld']    # 国内城市/热门城市/全部城市
        self.__search_type = self.SearchType.AllChina
        self.__citylist = {}        # 用来缓存指定搜索类型的城市列表
        self.__weather = {}         # 用来缓存指定城市的天气信息，需要间隔更新
        self.__url_weather = 'https://api.heweather.com/x3/weather'
        self.__key = '59b0c90752ff4d67ace5bf52c9df90cc'
        self.__city = city

    @unique                # @unique装时期可以检查保证没有重复值
    class SearchType(Enum):
        AllChina = 0       # 国内城市
        HotWorld = 1       # 热门城市
        AllWorld = 2       # 全部城市

    @staticmethod          # 静态方法
    def handle_request(url):
        req = request.Request(url)
        with request.urlopen(req) as response:
            logd('Status: ', response.status, response.reason)
            return response.read().decode('utf-8')

    def get_citylist(self, search_type=SearchType.AllChina):
        # 如果此次搜索的类型和上次的一样并且缓存的数据不为空，则直接返回，否则更新为最新的此次搜索类型
        if self.__search_type == search_type and len(self.__citylist):     # len(self.__citylist) is not 0
            logd('directly return the stored data...')
            return self.__citylist
        self.__search_type = search_type
        logd('start a http request for citylist...')
        # search_type.value = 0
        url = '%s?search=%s&key=%s' % (self.__url_citylist, self.__search[search_type.value], self.__key)
        self.__citylist = self.handle_request(url)
        return self.__citylist

    def get_weather(self, city=''):
        if city is not None:
            self.__city = city
        url = '%s?city=%s&key=%s' % (self.__url_weather, self.__city, self.__key)
        logd('start a http request for specific city weather...')
        self.__weather = self.handle_request(url)
        return self.__weather


if __name__ == '__main__':
    weather = Weather()
    # logd('citylist: ', weather.get_citylist())     # 第一次需要建立http请求
    # logd('citylist: ', weather.get_citylist())     # 第二次则直接返回存储的数据
    logd('citylist: ', weather.get_citylist(Weather.SearchType.HotWorld))  # 第三次因更改搜索类型，重新请求获取新的数据
    logd('-------------------------------------------------------------')
    logd('weather: ', weather.get_weather('shenzhen'))
	