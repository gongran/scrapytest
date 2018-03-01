from selenium import webdriver

class BlockChain:
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.urls=[
            'https://coinmarketcap.com/zh/exchanges/okex/',
            'https://coinmarketcap.com/zh/exchanges/binance/',
            'https://coinmarketcap.com/zh/exchanges/huobi/',
            'https://coinmarketcap.com/zh/exchanges/upbit/',
            'https://coinmarketcap.com/zh/exchanges/bitfinex/',
            'https://coinmarketcap.com/zh/exchanges/bithumb/',
            'https://coinmarketcap.com/zh/exchanges/bittrex/',
            'https://coinmarketcap.com/zh/exchanges/gdax/',
            'https://coinmarketcap.com/zh/exchanges/kraken/',
            'https://coinmarketcap.com/zh/exchanges/hitbtc/',
            'https://coinmarketcap.com/zh/exchanges/bit-z/',
            'https://coinmarketcap.com/zh/exchanges/bitstamp/',
            'https://coinmarketcap.com/zh/exchanges/zaif/',
            'https://coinmarketcap.com/zh/exchanges/poloniex/',
            'https://coinmarketcap.com/zh/exchanges/coinegg/'
           ]
        self.marketMap={}
    def fenxi(self):
        # 使用set得到去重后的币种
        ss=set()
        for url in self.urls:
            print(url)
            marketName=url[:-1]
            marketName=marketName[marketName.rfind('/')+1:]
            self.driver.get(url)
            i=0
            html=self.driver.find_elements_by_xpath('//*[@id="exchange-markets"]/tbody/tr/td[2]/a')
            while i<len(html):
                name=html[i].text
                ss.add(name)
                i+=1
            self.marketMap[marketName]=ss
        print(self.marketMap)
if __name__ == "__main__":
    cs = BlockChain()
    cs.fenxi()