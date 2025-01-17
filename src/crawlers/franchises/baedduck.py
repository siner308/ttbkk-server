import time
from src.apps.place.models import Place
from src.crawlers.base import BaseCrawler
from src.utils.chromedriver import setup_chrome
from src.utils.map import get_latlng
from selenium.webdriver.common.by import By


class BaeDduckCrawler(BaseCrawler):
    base_url = 'http://baedduck.co.kr/subpage/storeinfo?loc=&search=&page='
    page_number = 1
    brand = None

    def __init__(self):
        self.brand_name = '배떡'

    def set_next_page(self):
        self.url = self.base_url + str(self.page_number)
        is_success = False
        while not is_success:
            try:
                self.driver.get(self.url)
                time.sleep(3)
            except Exception as e:
                self.driver = setup_chrome()
                continue
            is_success = True
        self.page_number += 1

    def get_place_data(self):
        try:
            elements = self.driver.find_elements(by=By.XPATH, value=('//*[@id="wrap"]/section/div/table/tbody/tr'))
        except:
            print('추가 데이터가 없습니다.')
            return []
        places = []
        for element in elements:
            place_name = str(element.find_element(by=By.XPATH, value='./td[1]').text)

            if place_name.startswith('배떡  '):
                place_name = place_name.split('배떡  ')[1]
            elif place_name.startswith('배떡 '):
                place_name = place_name.split('배떡 ')[1]
            elif place_name.startswith('배떡'):
                place_name = place_name.split('배떡')[1]
            elif place_name.startswith('배덕 '):
                place_name = place_name.split('배덕 ')[1]
            elif place_name.startswith('배덕'):
                place_name = place_name.split('배덕')[1]
            elif place_name.startswith('배달떡볶이 '):
                place_name = place_name.split('배달떡볶이 ')[1]
            elif place_name.startswith('배달떡볶이'):
                place_name = place_name.split('배달떡볶이')[1]

            if place_name.startswith('('):
                place_name = place_name.split('(')[1]
            if place_name.startswith(')'):
                place_name = place_name.split(')')[1]

            if not place_name.endswith('점'):
                place_name += '점'

            region_name = str(element.find_element(by=By.XPATH, value='./td[2]').text)

            if region_name in place_name:
                name = '%s %s' % (self.brand_name, place_name)
            else:
                name = '%s %s %s' % (self.brand_name, region_name, place_name)
            print(name)
            address = element.find_element(by=By.XPATH, value='./td[3]').text
            latitude, longitude = get_latlng(address, name)
            if not latitude or not longitude:
                print('[failed] %s\n%s' % (name, address))
                continue

            places.append(Place(name=name, address=address, latitude=latitude, longitude=longitude,
                                brand=self.get_brand()))
            time.sleep(0.5)
        return places
