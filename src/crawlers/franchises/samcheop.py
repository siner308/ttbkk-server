import time
from src.apps.place.models import Place
from src.crawlers.base import BaseCrawler
from src.utils.chromedriver import setup_chrome
from src.utils.map import get_latlng
from selenium.webdriver.common.by import By


class SamCheopCrawler(BaseCrawler):
    base_url = 'http://www.samcheop.com/pg/bbs/board.php?bo_table=store01&page='
    page_number = 1
    brand = None

    def __init__(self):
        self.brand_name = '삼첩분식'

    def set_next_page(self):
        self.url = self.base_url + str(self.page_number)
        is_success = False
        while not is_success:
            try:
                self.driver.get(self.url)
                time.sleep(3)
            except Exception as e:
                print(e)
                self.driver = setup_chrome()
                continue
            is_success = True
        self.page_number += 1

    def get_place_data(self):
        elements = self.driver.find_elements(by=By.XPATH, value=('//*[@id="fboardlist"]/div/table/tbody/tr'))
        try:
            if elements[0].find_element(by=By.CLASS_NAME, value='empty_table'):
                print('추가 데이터가 없습니다.')
                return []
        except:
            pass

        places = []
        for element in elements:
            region_name = str(element.find_element(by=By.XPATH, value='./td[1]/a').text)
            place_name = str(element.find_element(by=By.XPATH, value='./td[2]/div/a/div[2]').text)
            telephone = element.find_element(by=By.XPATH, value='./td[4]/div[2]').text
            address = element.find_element(by=By.XPATH, value='./td[3]/div[2]').text
            print(place_name)

            if region_name == '프리미엄[홀]':
                address_region = address.split(' ')[0]
                if len(address_region) < 2:
                    region_name = ''
                elif len(address_region) >= 5:
                    # ex) 서울특별시, 부산광역시, 대구광역시, 인천광역시, 광주광역시, 대전광역시, 울산광역시, 세종특별자치시
                    region_name = address_region[:2]
                elif len(address_region) == 4:
                    # ex) 경상북도, 경상남도, 전라북도, 전라남도
                    region_name = address_region[:2]
                elif len(address_region) == 3:
                    # ex) 강원도, 경기도
                    region_name = address_region[:2]
                elif address_region == '해외':
                    region_name = ''
                else:
                    region_name = address_region[:2]

            if region_name in place_name:
                name = '%s %s' % (self.brand_name, place_name)
            else:
                name = '%s %s %s' % (self.brand_name, region_name, place_name)
            latitude, longitude = get_latlng(address, name)
            if not latitude or not longitude:
                print('[failed] %s\n%s\n%s' % (name, address, telephone))
                continue

            places.append(Place(name=name, address=address, latitude=latitude, longitude=longitude,
                                telephone=telephone, brand=self.get_brand()))
            time.sleep(0.5)
        return places
