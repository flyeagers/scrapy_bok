from lxml import etree
import requests
import time

for a in range(100):
    url = 'https://book.douban.com/top250?start=[]'.format(a*25)
    data = requests.get(url).text

    s = etree.HTML(data)
    #file = s.xpath(u"//[@id='content']/div/div[1]/table")
    file = s.xpath("//div[@id='content']/div/div[1]/div/table")
    #file = s.xpath(u"//div[@id='wrapper']/div[@id='content']/div/div[1]")
    time.sleep(3)

    for div in file:
        title = div.xpath('./tr/td[2]/div[1]/a/@title')[0].encode('utf-8')
        href = div.xpath('./tr/td[2]/div[1]/a/@href')[0].encode('utf-8')
        score = div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0].encode('utf-8')
        num = div.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip("(").strip(")").strip().encode('utf-8')
        scrible = div.xpath('./tr/td[2]/p[2]/span/text()')[0].encode('utf-8')

        if len(scrible) > 0:
            # print "{}.{}.{}.{}.{}\n".format(title, href, score, num, scrible[0])
            print "{}, {}, {}, {}, {}".format(title, href, score, num, scrible)
        else:
            print "{}.{}.{}.{}".format(title, href, score, num)
