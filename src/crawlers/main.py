from enum import Enum

from src.crawlers.franchises.baedduck import BaeDduckCrawler
from src.crawlers.franchises.gamtan import GamtanCrawler
from src.crawlers.franchises.myungranghotdog import MyungrangHotDogCrawler
from src.crawlers.franchises.sinbul import SinBulCrawler
from src.crawlers.franchises.sincham import SinChamCrawler
from src.crawlers.franchises.sinjeon import SinjeonCrawler
from src.crawlers.franchises.youngdabang import YoungDaBangCrawler
from src.crawlers.franchises.yupdduk import YupddukCrawler


class FranchiseType(Enum):
    SINJEON = '신전'
    GAMTAN = '감탄'
    YUPDDUK = '엽떡'
    BAEDDUCK = '배떡'
    MYUNGRANG = '명랑'
    YOUNGDABANG = '청년다방'
    SINCHAM = '신참'
    SINBUL = '신불'


def get_crawlers(types):
    result = []
    for crawler_type in types:
        if crawler_type == FranchiseType.SINJEON:
            result.append(SinjeonCrawler())
        elif crawler_type == FranchiseType.GAMTAN:
            result.append(GamtanCrawler())
        elif crawler_type == FranchiseType.YUPDDUK:
            result.append(YupddukCrawler())
        elif crawler_type == FranchiseType.BAEDDUCK:
            result.append(BaeDduckCrawler())
        elif crawler_type == FranchiseType.MYUNGRANG:
            result.append(MyungrangHotDogCrawler())
        elif crawler_type == FranchiseType.YOUNGDABANG:
            result.append(YoungDaBangCrawler())
        elif crawler_type == FranchiseType.SINCHAM:
            result.append(SinChamCrawler())
        elif crawler_type == FranchiseType.SINBUL:
            result.append(SinBulCrawler())
        else:
            raise TypeError('invalid crawler type')
    return result


def run():
    crawlers = get_crawlers([
        # FranchiseType.SINJEON,
        # FranchiseType.GAMTAN,
        # FranchiseType.YUPDDUK,
        # FranchiseType.BAEDDUCK,
        # FranchiseType.MYUNGRANG,
        # FranchiseType.YOUNGDABANG,
        # FranchiseType.SINCHAM,
        FranchiseType.SINBUL,
    ])
    for crawler in crawlers:
        crawler.run()
