from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 初始化 Chrome 瀏覽器
driver = webdriver.Chrome()

# 打開瀏覽器並前往國泰世華銀行網頁
driver.get("https://www.cathaybk.com.tw/cathaybk/")

# 網頁視窗最大化
driver.maximize_window()

#休息兩秒抓取定位
time.sleep(2)

# 定位並點擊"產品介紹"欄位
try:
    product_intro_link = driver.find_element(by=By.XPATH, value="//*[contains(text(),'產品介紹')]")
    product_intro_link.click()
    time.sleep(1)
    print("點擊產品介紹：成功")
except:
    print("點擊產品介紹：失敗")


# 定位並點擊"貸款試算"字串
try:
    loan_calculator_link = driver.find_element(by=By.XPATH, value="//*[contains(text(),'貸款試算')]")
    loan_calculator_link.click()
    time.sleep(1)
    print("點擊貸款試算：成功")
except:
    print("點擊貸款試算：失敗") 

# 定位並點擊"信用貸款試算"裡面的"每月還款試算"
try:
    credit_loan_link = driver.find_element(by=By.CLASS_NAME,value="cubinvest-bold-title")
    credit_loan_link.click()
    time.sleep(1)
    print("點擊每月還款試算：成功")
except:
    print("點擊每月還款試算：失敗") 

# 定位貸款金額、相關費用、利率計算方式輸入框，並輸入相應的數值
try:
    loan_amount_input = driver.find_element(By.ID, "amount")
    loan_amount_input.send_keys("1000")
    time.sleep(1)
    print("輸入貸款金額：成功")
except:
    print("輸入貸款金額：失敗") 

try:
    related_cost_input = driver.find_element(By.ID, "Fee")
    related_cost_input.send_keys("5000")
    time.sleep(1)
    print("輸入相關費用：成功")
except:
    print("輸入相關費用：失敗") 

try:
    interest_rate_input = driver.find_element(By.ID, "periodrate1")
    interest_rate_input.send_keys("1.38")
    time.sleep(1)
    print("輸入利率：成功")
except:
    print("輸入利率：失敗") 

# 定位並點擊"開始試算"按鈕
try:
    start_calculation_button = driver.find_element(By.ID, "formSubmitBtn")
    start_calculation_button.click()
    time.sleep(1)
    print("點擊開始試算：成功")
except:
    print("點擊開始試算：失敗") 


# 定位到元素並驗證貸款金額
try:
    loan_amount = driver.find_element(by=By.CLASS_NAME, value="cubinvest-normal-p")
    expected_loan_amount = "您的貸款金額： 1,000萬元"
    assert loan_amount.text == expected_loan_amount
    print("貸款金額：驗證成功！")
except AssertionError:
    print("貸款金額：驗證失敗！")

# 定位並驗證總費用年百分率
try:
    apr=driver.find_element(By.XPATH, '//*[@id="mainform"]/div[4]/main/div/div[3]/div/section/div/div/div[1]/div[1]/div[2]/span')
    expected_apr = "1.41%"
    assert apr.text == expected_apr
    print("總費用年百分率：驗證成功！")
except AssertionError:
    print("總費用年百分率：驗證失敗！")

# 定位並驗證第1 ~ 35個月每期應還本利和
try:
    month_1_to_35 = driver.find_element(by=By.CLASS_NAME, value="cubinvest-highlight")
    expected_month_1_to_35 = "283,727"
    assert month_1_to_35.text == expected_month_1_to_35
    print("第1至35個月每期應還本利和：驗證成功！")
except AssertionError:
    print("第1至35個月每期應還本利和：驗證失敗！")


# 定位並驗證第36個月每期應還本利和
try:
    month_36= driver.find_element(By.XPATH, '//*[@id="mainform"]/div[4]/main/div/div[3]/div/section/div/div/div[1]/div[2]/div/div/div[2]/div[2]/span')
    expected_month_36 = "283,732"
    assert month_36.text == expected_month_36
    print("第36個月每期應還本利和：驗證成功！")
except AssertionError:
    print("第36個月每期應還本利和：驗證失敗！")

# 以上所有的assert語句都沒有引發AssertionError，則代表測試通過
print("全數驗證通過. Test successful.")

# 關閉瀏覽器
driver.quit()










# # 驗證欄位是否顯示正確的值
# try:
#     # 使用顯式等待等待結果顯示
#     result = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "result"))
#     )
    
#     # 驗證貸款金額
#     assert "1000萬元" in result.text
    
#     # 驗證總費用年百分率
#     assert "1.41%" in result.text
    
#     # 驗證費用部分
#     expected_monthly_payments = ["283,727"] * 35 + ["283,732"]
#     monthly_payment_elements = driver.find_elements_by_xpath("//div[@class='table']/table/tbody/tr[2]/td")
#     for i, element in enumerate(monthly_payment_elements):
#         assert element.text == expected_monthly_payments[i]

#     print("驗證成功！")
# except AssertionError:
#     print("驗證失敗！")

# 關閉瀏覽器
#driver.quit()