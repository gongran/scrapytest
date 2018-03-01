import json
class HuoBiCompare:
    def __init__(self):
        self.marketMap={}

    def compareCoin(self):
        aa={}
        with open("coins.txt",'r') as fileReade:
            while True:
                lines=fileReade.readline()
                if not lines:
                    break
                    pass
                lines=lines.replace('\'','\"')
                aa=json.loads(lines)
        huobi=list()
        huobi=aa['huobi']
        allqubie=list()
        for key in aa:
            print(key)
            kklist=aa[key]
            qubie=list()
            for name in kklist:
                if name not in huobi:
                    qubie.append(name)
            print(qubie)
            allqubie=allqubie+qubie
            # print(aa[key])
            print("--------------------------------------------------------------")
        print("排名前20交易所有而火币网没有的币种 共"+str(len(set(allqubie)))+"个：")
        print(set(allqubie))
if __name__ =="__main__":
    cl=HuoBiCompare()
    cl.compareCoin()