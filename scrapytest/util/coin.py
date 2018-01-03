from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class coin:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome("D:\\rt\\chromedriver.exe")
        # driver = webdriver.PhantomJS("D:\\rt\\phantomjs.exe")
        driver.get("https://www.huobi.pro/zh-cn/assetintro")
        try:
            html = driver.find_elements_by_xpath("//div[@class='sider_flow']/dd")
            # html = WebDriverWait(driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, "//div[@class='sider_flow']/dd")))
            i = 0
            while i < len(html):
                yx = html[i]
                # title = yx.get_attribute("data-coin")
                cname = yx.find_elements_by_xpath("span")
                print(cname[0].text+" "+cname[1].text)
                i += 1
        finally:
            driver.quit()


if __name__ == '__main__':
    coin()
