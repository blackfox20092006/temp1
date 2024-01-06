# import random
#
# from requests import get
# char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# email = f'{"".join([random.choice(char) for i in range(20)])}%40gmail.com'
# response_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdJMlYDEQzWSffoZqc5C2x00DD_gBKrnqKxZ1CXT94grlLrKw/formResponse?&submit=Submit?usp=pp_url&'
# url1 = response_url + f'entry.425689288={email}&dlut=1704527392429&hud=true&fvv=1&partialResponse=%5Bnull%2Cnull%2C%22-3058505899846443617%22%5D&pageHistory=0&fbzx=-8548649952057787397&continue=1'
# url2 = response_url + f'entry.925837225=from+12A7+with+love&entry.1595986993=12A7&entry.1220711105=N%E1%BB%AF&entry.1228003864=Kh%E1%BB%91i+12&entry.1826461630.other_option_response=tr%C6%B0%E1%BB%9Dng+%C4%91%E1%BB%9Di&entry.1826461630=__other_option__&entry.1722009187.other_option_response=tr%C6%B0%E1%BB%9Dng+%C4%91%E1%BB%9Di&entry.1722009187=__other_option__&entry.1545496035.other_option_response=tr%C6%B0%E1%BB%9Dng+%C4%91%E1%BB%9Di&entry.1545496035=__other_option__&dlut=1704527480289&entry.1220711105_sentinel=&entry.1228003864_sentinel=&entry.1826461630_sentinel=&entry.1722009187_sentinel=&entry.1545496035_sentinel=&fvv=1&partialResponse=%5B%5B%5Bnull%2C425689288%2C%5B%22{email}%22%5D%2C0%5D%5D%2Cnull%2C%22-8548649952057787397%22%5D&pageHistory=0%2C1&fbzx=-8548649952057787397&continue=1'
# url3 = response_url + f'entry.297652059=tr%C6%B0%E1%BB%9Dng+%C4%91%E1%BB%9Di&entry.724256113=Kh%C3%B4ng+quan+tr%E1%BB%8Dng&entry.418081648=Kh%C3%B4ng+quan+tr%E1%BB%8Dng&entry.734466504=Kh%C3%B4ng+quan+tr%E1%BB%8Dng&entry.1461470919=Kh%C3%B4ng+quan+tr%E1%BB%8Dng&entry.2048937485=Kh%C3%B4ng+quan+tr%E1%BB%8Dng&dlut=1704527536379&entry.724256113_sentinel=&entry.418081648_sentinel=&entry.734466504_sentinel=&entry.1461470919_sentinel=&entry.2048937485_sentinel=&fvv=1&partialResponse=%5B%5B%5Bnull%2C425689288%2C%5B%22{email}%22%5D%2C0%5D%2C%5Bnull%2C925837225%2C%5B%22from+12A7+with+love%22%5D%2C0%5D%2C%5Bnull%2C1220711105%2C%5B%22N%E1%BB%AF%22%5D%2C0%5D%2C%5Bnull%2C1228003864%2C%5B%22Kh%E1%BB%91i+12%22%5D%2C0%5D%2C%5Bnull%2C1595986993%2C%5B%2212A7%22%5D%2C0%5D%2C%5Bnull%2C1826461630%2C%5B%22tr%C6%B0%E1%BB%9Dng+%C4%91%E1%BB%9Di%22%5D%2C1%5D%2C%5Bnull%2C1722009187%2C%5B%22tr%C6%B0%E1%BB%9Dng+%C4%91%E1%BB%9Di%22%5D%2C1%5D%2C%5Bnull%2C1545496035%2C%5B%22tr%C6%B0%E1%BB%9Dng+%C4%91%E1%BB%9Di%22%5D%2C1%5D%5D%2Cnull%2C%22-8548649952057787397%22%5D&pageHistory=0%2C1%2C2&fbzx=-8548649952057787397&continue=1'
# url4 = response_url + f'entry.2089755169=0923450850&entry.930550319=0923450850&entry.1203853977=giang+h%E1%BB%93&entry.1915367385=li%c3%aan%20h%e1%bb%87%20telegram%200923450850&entry.557022990={random.randint(111111111111,999999999999)}&dlut=1704527611017&fvv=1&partialResponse=%5B%5B%5Bnull%2C425689288%2C%5B%22{email}%22%5D%2C0%5D%2C%5Bnull%2C925837225%2C%5B%22from+A7+with+love%22%5D%2C0%5D%2C%5Bnull%2C1220711105%2C%5B%22N%E1%BB%AF%22%5D%2C0%5D%2C%5Bnull%2C1228003864%2C%5B%22Kh%E1%BB%91i+12%22%5D%2C0%5D%2C%5Bnull%2C1595986993%2C%5B%2212A7%22%5D%2C0%5D%2C%5Bnull%2C1826461630%2C%5B%22tr%C6%B0%E1%BB%9Dng+%C4%91%E1%BB%9Di%22%5D%2C1%5D%2C%5Bnull%2C1722009187%2C%5B%22tr%C6%B0%E1%BB%9Dng+%C4%91%E1%BB%9Di%22%5D%2C1%5D%2C%5Bnull%2C1545496035%2C%5B%22tr%C6%B0%E1%BB%9Dng+%C4%91%E1%BB%9Di%22%5D%2C1%5D%2C%5Bnull%2C297652059%2C%5B%22tr%C6%B0%E1%BB%9Dng+%C4%91%E1%BB%9Di%22%5D%2C0%5D%2C%5Bnull%2C724256113%2C%5B%22Kh%C3%B4ng+quan+tr%E1%BB%8Dng%22%5D%2C0%5D%2C%5Bnull%2C418081648%2C%5B%22Kh%C3%B4ng+quan+tr%E1%BB%8Dng%22%5D%2C0%5D%2C%5Bnull%2C734466504%2C%5B%22Kh%C3%B4ng+quan+tr%E1%BB%8Dng%22%5D%2C0%5D%2C%5Bnull%2C1461470919%2C%5B%22Kh%C3%B4ng+quan+tr%E1%BB%8Dng%22%5D%2C0%5D%2C%5Bnull%2C2048937485%2C%5B%22Kh%C3%B4ng+quan+tr%E1%BB%8Dng%22%5D%2C0%5D%5D%2Cnull%2C%22-8548649952057787397%22%5D&pageHistory=0%2C1%2C2%2C3&fbzx=-8548649952057787397'
# print(url1)
# print(url2)
# print(url3)
# print(url4)
from selenium.webdriver.common.by import By
import threading,random
from time import sleep
with open('name.txt') as f:
    name = [i.replace('\n', '') for i in f.readlines()]
f.close()
with open('ua.txt') as ff:
    ua = [i.replace('\n', '') for i in ff.readlines()]
ff.close()
from selenium import webdriver
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
email = f'{"".join([random.choice(char) for i in range(20)])}@gmail.com'
from selenium.webdriver.support.ui import WebDriverWait
def runnow(n):
    def calculate_window_position(window_index):
        window_width = 30  # Chiều rộng của cửa sổ
        window_height = 200  # Chiều cao của cửa sổ
        spacing = 150  # Khoảng cách giữa các cửa sổ theo chiều ngang
        num_windows_per_row = 6  # Số lượng cửa sổ trên mỗi hàng
        row_index = window_index // num_windows_per_row
        column_index = window_index % num_windows_per_row
        x = column_index * (window_width + spacing)
        y = row_index * (window_height + spacing - 100)
        return x, y
    def find_until_xpath(driver, name, status, content):
        e = None
        for i in range(100):
            try:
                sleep(0.2)
                e = driver.find_element(By.XPATH, name)
                break
            except:
                continue
        for i in range(200):
            try:
                if status == 0:
                    e.click()
                elif status == 1:
                    e.send_keys(content)
                return
            except:
                sleep(0.2)
                continue
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('log-level=3')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--disable-default-apps')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--disable-media-source")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-webgl")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_argument("--disable-accelerometer")
    chrome_options.add_argument("--disable-bluetooth")
    chrome_options.add_argument("--disable-printing")
    chrome_options.add_argument("--disable-ambient-light-sensor")
    chrome_options.add_argument("--disable-web-authentication")
    chrome_options.add_argument("--disable-gamepad")
    chrome_options.add_argument("--disable-midi")
    chrome_options.add_argument("--disable-usb")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument("--disable-webrtc")
    chrome_options.add_argument("--disable-canvas-aa")
    chrome_options.add_argument("--disable-2d-canvas-clip-aa")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument(f'--user-agent="{random.choice(ua)}"')
    chrome_options.add_argument("--app=https://docs.google.com/forms/d/e/1FAIpQLSdJMlYDEQzWSffoZqc5C2x00DD_gBKrnqKxZ1CXT94grlLrKw/viewform")
    chrome_options.add_argument("--disable-credentials_enable_service")
    chrome_options.add_argument("--disable-profile.password_manager_enabled")
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    x, y = calculate_window_position(n)
    driver.set_window_rect(x, y, 30, 200)
    WebDriverWait(driver, timeout=10)
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input', 1, email)
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span', 0, '')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, random.choice(name) + ' ' + random.choice(name) + ' ' + random.choice(name))
    e = find_until_xpath(driver, '//*[@id="i12"]/div[3]/div', 0, '')
    e = find_until_xpath(driver, '//*[@id="i19"]/div[3]/div', 0, '')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, 'From 12A7 with love')
    e = find_until_xpath(driver, '//*[@id="i48"]/div[3]/div', 0, '')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[7]/div/span/div/div/div[1]/input', 1,'trường đời')
    e = find_until_xpath(driver, '//*[@id="i169"]/div[3]/div', 0, '')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[39]/div/span/div/div/div[1]/input', 1, 'trường đời')
    e = find_until_xpath(driver, '//*[@id="i290"]/div[3]/div', 0, '')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[39]/div/span/div/div/div[1]/input', 1, 'trường đời')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span', 0, '')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, 'trường đời')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div', 0, '')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div', 0, '')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div', 0, '')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div', 0, '')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div', 0, '')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span', 0, '')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, '02837125691')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, '02837125691')
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, 'giang hồ')
    tinh_thanh_vietnam = [
        "An Giang",
        "Bà Rịa - Vũng Tàu",
        "Bạc Liêu",
        "Bắc Kạn",
        "Bắc Giang",
        "Bắc Ninh",
        "Bến Tre",
        "Bình Dương",
        "Bình Định",
        "Bình Phước",
        "Bình Thuận",
        "Cà Mau",
        "Cao Bằng",
        "Cần Thơ",
        "Đà Nẵng",
        "Đắk Lắk",
        "Đắk Nông",
        "Điện Biên",
        "Đồng Nai",
        "Đồng Tháp",
        "Gia Lai",
        "Hà Giang",
        "Hà Nam",
        "Hà Nội",
        "Hà Tĩnh",
        "Hải Dương",
        "Hải Phòng",
        "Hậu Giang",
        "Hòa Bình",
        "Hưng Yên",
        "Khánh Hòa",
        "Kiên Giang",
        "Kon Tum",
        "Lai Châu",
        "Lâm Đồng",
        "Lạng Sơn",
        "Lào Cai",
        "Long An",
        "Nam Định",
        "Nghệ An",
        "Ninh Bình",
        "Ninh Thuận",
        "Phú Thọ",
        "Phú Yên",
        "Quảng Bình",
        "Quảng Nam",
        "Quảng Ngãi",
        "Quảng Ninh",
        "Quảng Trị",
        "Sóc Trăng",
        "Sơn La",
        "Tây Ninh",
        "Thái Bình",
        "Thái Nguyên",
        "Thanh Hóa",
        "Thừa Thiên Huế",
        "Tiền Giang",
        "Trà Vinh",
        "Tuyên Quang",
        "Vĩnh Long",
        "Vĩnh Phúc",
        "Yên Bái"
    ]
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, random.choice(tinh_thanh_vietnam))
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, str(random.randint(111111111111, 999999999999)))
    e = find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span', 0, '')
    for i in range(200):
        try:
            e = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            return
        except:
            sleep(0.2)
            continue
threadnum = int(input('Số luồng : '))
while True:
    threads = []
    for i in range(threadnum):
        threads.append(threading.Thread(target=runnow, args=(i,)))
    for i in range(threadnum):
        threads[i].start()
        sleep(1)
    for i in range(threadnum):
        threads[i].join()
