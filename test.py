import requests
from bs4 import BeautifulSoup

# 函數用於從網站上獲取即時匯率表
def get_exchange_rates():
    url = "https://www.cathaybk.com.tw/cathaybk/personal/deposit-exchange/rate/currency-billboard/?indexwidget"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        #print(soup.prettify()) 
        currency_elements=soup.find_all("div", class_="cubre-m-currency__name")
        #print(currency)

    
    # 獲取客戶輸入的貨幣名稱
        user_input = input("請輸入您想要查找的貨幣名稱：")

    # 宣告變數count
    count = 0
    # 宣告變數found，用於標記是否找到符合條件的匯率
    found = False
    # 獲取 currency_elements 列表的長度
    list_length = len(currency_elements)

    # 循環開始
    for count in range(list_length):
        currency = currency_elements[count]
        #print(currency)
        # 打印當前 count 的值
        #print("當前 count 的值是：", count)

        if user_input in currency.get_text():
            # print("找到了用戶輸入的内容！")
            # 如果找到了就停止循環
            found = True
            break
        # 在每次循環中，count 加 1
        # count += 1

    if not found:
        print("錯誤：找不到符合條件的匯率")
        exit()


    #print(count)
    table = soup.find_all("div", class_="cubre-o-table__item currency")[count]

    
    if table:
        #print(table)
        name = table.find("div", class_="cubre-m-currency__name").text.strip()
        #print(name)
        rows = table.find_all("tr")
        headers = [header.text.strip() for header in rows[0].find_all("div", class_="cubre-m-rateTable__th -en")]
        data = []
        for row in rows[1:]:
            values = [value.text.strip() for value in row.find_all("div")]
            data.append(dict(zip(headers, values)))
        return name, data
    else:
        print("找不到匯率表")
        return None, None  # 返回None以表明找不到匯率表

# 函數用於打印匯率表
def print_exchange_rates(currency_name, rates):
    print("幣別:", currency_name)
    for rate in rates:
        print("項目:", rate.get("Item", "N/A"))
        print("銀行買進:", rate.get("Bank buy", "N/A"))
        print("銀行賣出:", rate.get("Bank sell", "N/A"))
        print("========================================")
    #print(rate)
    #print(rates)
    #print(currency_name)

    # 輸出客戶輸入的貨幣名稱
    method = input("請輸入兌換的項目（即期匯率模式、數位通路優惠匯率、現鈔匯率模式）：")
    #print(method)
    #print(rates)

    count = 0
    found = False

    for rate in rates:
        #print("項目:", rate.get("Item", "N/A"))  
        item=rate.get("Item")
        #print(111111111) 
        if method in item:
            found = True
            break
        count += 1



    twd_amount_str = input("請輸入您要兌換的新台幣金額：")
    twd_amount = float(twd_amount_str)
    #print(twd_amount)

    # 假設 rate.get("Bank sell", "N/A") 返回的是字符串
    #bank_sell_str = rate.get("Bank sell", "N/A")
    
    
    # print(rate)
    # print(count)
    # print(rates[count])
    # print(22222222222222)
    bank_sell_str = rates[count].get("Bank sell")
    print(bank_sell_str)


# 確認是否成功轉換
    if  bank_sell_str != "--":
        bank_sell_rate = float(bank_sell_str)
        foreign_output = twd_amount / bank_sell_rate
        rounded_output = round(foreign_output, 2) 
        print("兌換後的外幣金額為:", rounded_output)
    else:
        print("錯誤：無法有效取得銀行賣出匯率")


    
# 主程式
if __name__ == "__main__":
    # 取得匯率表
    currency_name, exchange_rates = get_exchange_rates()
    if exchange_rates:
        # 印出匯率表
        print_exchange_rates(currency_name, exchange_rates)
        



