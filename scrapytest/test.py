import time

from scrapytest.item.WaiHuiItems import WaiHuiItem

aa = WaiHuiItem()
print(type(aa))
if type(aa) == WaiHuiItem:
    print(123)
else:
    print(666)
timeStr=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(timeStr)
