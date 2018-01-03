from scrapy import cmdline
import schedule
import time
import subprocess

def crawl_work():
    name = 'HangQing'
    # name = 'MySpider'
    cmd = 'scrapy crawl {0}'.format(name)
    # cmdline.execute(cmd.split())
    subprocess.Popen(cmd)
    print(123)

if __name__=='__main__':
    schedule.every(1).minutes.do(crawl_work)
    while True:
         schedule.run_pending()
         time.sleep(1)