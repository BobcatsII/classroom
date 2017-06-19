# -*- coding: utf8 -*-
import urllib2
import json

while True:
    cityname = raw_input('你想查哪个城市的天气？(支持汉字/拼音)\n')                                                                  #.decode('utf8').encode('gb18030')
    if cityname:
        try:
            url = ('https://free-api.heweather.com/v5/weather?key=bb18bc76597a48e5ac978ea7aac9448b&city=%s' % cityname)
            content = urllib2.urlopen(url).read()
            data = json.loads(content)
            #print data
            result = data['HeWeather5']
            str_temp = ('%s' % result['now'])
            print str_temp
            choice = raw_input('想要继续查询吗？Y/N')
            if choice == 'y' or choice == 'Y':
                continue
            elif choice == 'n' or choice == 'N':
                break
        except:
            print ('查询失败，请重新查询')
            continue
    else:
        print ('你输入的城市不存在,请重新输入！')
        continue

raw_input('若要退出，请按回车')
