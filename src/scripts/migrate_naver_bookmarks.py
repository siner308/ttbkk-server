import json
import os
import uuid

from src.apps.place.models import Place


def run(data: dict = {}, ttbkk_category_name: str = "떡볶이"):
    # filter by FranchiseType
    franchise_type_filtered_bookmarks = data.get('bookmarkList')

    places = []
    for bookmark in franchise_type_filtered_bookmarks:
        bookmarkId = bookmark.get("bookmarkId")  # : 1325377011,
        name = bookmark.get("name")  # : "레드175 대치역점",
        displayName = bookmark.get("displayName")  # : "",
        px = bookmark.get("px")  # : 127.0624408,
        py = bookmark.get("py")  # : 37.4938266,
        type = bookmark.get("type")  # : "place",
        useTime = bookmark.get("useTime")  # : 1701597577000,
        lastUpdateTime = bookmark.get("lastUpdateTime")  # : 1701597577000,
        creationTime = bookmark.get("creationTime")  # : 1701597577000,
        order = bookmark.get("order")  # : 65535,
        sid = bookmark.get("sid")  # : "1891657344",
        address = bookmark.get("address")  # : "서울 강남구 남부순환로 2942",
        memo = bookmark.get("memo")  # : null,
        url = bookmark.get("url")  # : null,
        mcid = bookmark.get("mcid")  # : "DINING",
        mcidName = bookmark.get("mcidName")  # : "음식점",
        rcode = bookmark.get("rcode")  # : "09680106",
        cidPath = bookmark.get("cidPath")  # : ["220036", "220048", "1005445"],
        available = bookmark.get("available")  # : true,
        folderMappings = bookmark.get("folderMappings")  # : null,
        placeInfo = bookmark.get("placeInfo")  # : null,
        isIndoor = bookmark.get("isIndoor")  # : true

        print(f"{name} - {address}")
        new_place = Place(
            id=uuid.uuid4().__str__().replace('-', ''),
            name=name,
            address=address,
            latitude=py,
            longitude=px,
        )
        places.append(new_place)

    result = Place.objects.bulk_create(objs=places)

    print(f"{len(result)}개의 장소가 추가되었습니다.")


def main():
    # category_name = '떡볶이'
    # BOOKMARK_CATEGORY_LIST_URL = 'https://pages.map.naver.com/save-pages/api/maps-bookmark/v3/folders?start=0&limit=20&sort=lastUseTime&folderType=all'
    # bookmark_category_data = requests.get(BOOKMARK_CATEGORY_LIST_URL).json()
    # ttbkk_folder = list(filter(lambda folder: folder.get('name') == category_name, bookmark_category_data.get('folders')))[0]

    # shared_id = '1eeeb00929fd4a33a383421fd363eb8f'
    # BOOKMARK_LIST_URL = f'https://pages.map.naver.com/save-pages/api/maps-bookmark/v3/shares/{shared_id}/bookmarks?start=0&limit=5000&sort=lastUseTime '
    # bookmark_data = requests.get(BOOKMARK_LIST_URL).json()

    with open(os.path.join(os.path.dirname(__file__), 'naver_bookmark.json'), 'r') as f:
        bookmark_data = json.load(f)

    run(data=bookmark_data, ttbkk_category_name="떡볶이")


if __name__ == "__main__":
    main()
