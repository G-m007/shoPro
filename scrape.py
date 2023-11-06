from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# import smtplib
from email.mime.text import MIMEText

# url = f"https://www.amazon.in/Apple-iPhone-13-128GB-Blue/dp/B09G9BL5CP/ref=sr_1_1_sspa?crid=34ACBT7YPE3AO&keywords=iphone+14&qid=1696822803&sprefix=iphone%2Caps%2C345&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument(f'user-agent={user_agent}')
# options.add_argument("--window-size=1920,1080")
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--allow-running-insecure-content')
# options.add_argument("--disable-extensions")
# options.add_argument("--proxy-server='direct://'")
# options.add_argument("--proxy-bypass-list=*")
# options.add_argument("--start-maximized")
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')
# driver = webdriver.Chrome('/Users/fardeenmac/Downloads/chromedriver',options=options)
# driver.get(url)
# wait = driver.implicitly_wait(5)


# ele = driver.find_element("xpath", '/html/body/div[4]/div/div[3]/div[11]/div[3]/div/h1/span');
# print(ele.text);


# import selenium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

url = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5T6CZ6/ref=sr_1_3?crid=2VMOKQNII27SS&keywords=mac&qid=1696836847&sprefix=iphone+14+pro%2Caps%2C1762&sr=8-3"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)

driver.get(url)
# ele = driver.find_element("xpath", '/html/body/div[4]/div/div[3]/div[11]/div[3]/div/h1/span')
ele2= driver.find_element("xpath", '/html/body/div[4]/div/div[3]/div[11]')
# print(ele.text)
print(ele2.text)
