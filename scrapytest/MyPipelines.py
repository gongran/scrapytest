import pymysql

from scrapytest.item.WaiHuiItems import WaiHuiItem


class MyPipeline(object):
    def __init__(self):
        # 打开文件
        self.file = open('data.json', 'w', encoding='utf-8')
        self.db = pymysql.connect("localhost", "root", "root", "market")

    # 该方法用于处理数据
    def process_item(self, item, spider):
        cursor = self.db.cursor()
        if type(item) == WaiHuiItem:
            zhujian = item["name"]
            jiage = item["price"]
            sql = "update sys_param set param_value=%s where param_name=%s"
        try:
            # 执行sql语句
            cursor.execute(sql, (jiage, zhujian))
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()

        # # 读取item中的数据
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # # 写入文件
        # self.file.write(line)
        # 返回item
        return item


# 该方法在spider被开启时被调用。
def open_spider(self, spider):
    print("111")


# 该方法在spider被关闭时被调用。
def close_spider(self, spider):
    print("222")
    self.db.close()
