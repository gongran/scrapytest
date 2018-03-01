# coding=utf-8

import time
import datetime
import pymysql
from selenium import webdriver

from scrapytest.util.CoinItem import CoinItem


class CommonSp:
    def __init__(self):
        url = []
        self.db = pymysql.connect("localhost", "root", "root", "market")
        self.driver = webdriver.PhantomJS()
        self.url = "https://www.huobipro.com/zh-cn/coin_coin/exchange/"
        self.crawlHb()

    def printHb(self, adress):
        if self.url.count(adress) > 0:
            print("已经存在")
        else:
            self.url.append(adress)
            print("不存在已经添加")

    def crawlHb(self):
        con = True
        while True:
            timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("开始时间:" + timeStr)
            handles = self.driver.window_handles
            if len(handles) > 1:
                print(self.driver.current_window_handle)
                self.driver.close()
            if con:
                self.driver.get(self.url)
                con = False
            else:
                newwindow = 'window.open("' + self.url + '");'
                print(newwindow)
                self.driver.switch_to_window(handles[-1])
                self.driver.execute_script(newwindow)
                handles = self.driver.window_handles

            try:
                html = self.driver.find_elements_by_xpath("//div[@class='coin_filter']/span[@action='userfilter']")
                i = 0
                coinItemList = []
                while i < len(html):
                    yx = html[i]
                    cp_type = yx.text
                    print(cp_type)
                    yx.click()
                    ch = self.driver.find_elements_by_xpath("//dl[@action='gourl']")
                    j = 0
                    while j < len(ch):
                        ci = CoinItem()
                        ci.cp_type = cp_type
                        yy = ch[j]
                        price = yy.find_elements_by_xpath(".//dd/div/div/span[2]")
                        cp_key = yy.find_elements_by_xpath(".//dd/div/div/span[1]/em")[0].text
                        ci.cp_key = cp_key
                        cp_name = yy.get_attribute("data-symbol")
                        cp_value = price[0].text
                        ci.cp_name = cp_name
                        ci.cp_value = cp_value
                        print(cp_name + ":" + cp_value)
                        j += 1
                        coinItemList.append(ci)
                    i += 1
                self.insertList(coinItemList)
            finally:
                # self.driver.quit()
                pass

    def insertList(self, list):
        self.db = pymysql.connect("localhost", "root", "root", "market")
        cursor = self.db.cursor()
        try:
            for cl in list:
                cp_name = cl.cp_name
                sql = "select * from coin_price where cp_name=%s"
                cursor.execute(sql, (cp_name))
                data = cursor.fetchone()
                dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if data:
                    sql = "update coin_price set cp_key=%s,cp_type=%s,cp_value=%s,cp_open=%s,cp_close=%s,cp_height=%s,cp_low=%s,last_ud=%s where cp_name=%s"
                    cursor.execute(sql,
                                   (cl.cp_key, cl.cp_type, cl.cp_value, cl.cp_open, cl.cp_close, cl.cp_height,
                                    cl.cp_low,dt, cl.cp_name))
                else:
                    sql = "insert into coin_price (cp_name,cp_key,cp_type,cp_value,cp_open,cp_close,cp_height,cp_low)values(%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql,
                                   (cl.cp_name, cl.cp_key, cl.cp_type, cl.cp_value, cl.cp_open, cl.cp_close,
                                    cl.cp_height,
                                    cl.cp_low))
            self.db.commit()
            self.db.close()
        except Exception as e:
            # 如果发生错误则回滚
            self.db.rollback()
            print(e)


if __name__ == "__main__":
    cs = CommonSp()
