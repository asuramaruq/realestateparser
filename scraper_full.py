import time
import random
import requests
from src.db.sessions import session
from src.db import schemas as db_sch
from src.db import services as db_srv
from sqlalchemy.exc import IntegrityError
from bs4 import BeautifulSoup
import concurrent.futures
import schedule

def get_data_scraper1(url):
    t_st = time.time()
    response = requests.get(url)
    t_res = round(time.time() - t_st, 2)
    data = dict()
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"ERROR::{response.status_code=}")

    return t_res, data, response.status_code


def scraper1(index):
    url = f'https://korter.kz/pyapi/map/building-card?building_id={index}&lang=ru-RU&locale=ru-RU'
    try:
        t_exec, data, status_code = get_data_scraper1(url)
        print(f"{url=} :: {t_exec=}")

        if status_code in [500, 504]:
            not_processed_scraper1.append(index)
            return

    except requests.exceptions.ConnectionError:
        time.sleep(5)
        t_exec, data, status_code = get_data_scraper1(url)
        print(f"[RETRY] :: {url=} :: {t_exec=}")

    if data is None:
        print(f"[NO_DATA]::{url=}")
        return

    data = data['data']['building']

    if data is None:
        print(f"[NO_BUILDING_DATA]::{url=}")
        return

    developers = data.pop('developers', [])
    labels = data.pop('labels', [])
    featureLabels = data.pop('featureLabels', [])
    images = data.pop('images', [])
    mainGeoObject = data.pop('mainGeoObject', None)
    location = data.pop('location', None)

    try:
        building = db_sch.TestBuilding(**data)
        session.add(building)

        if developers:
            for developer in developers:
                dd = db_sch.TestDeveloper(**developer)
                building.developers.append(dd)

        if location:
            ll = db_sch.TestLocation(**location)
            building.location = ll

        session.commit()
    except IntegrityError as e:
        session.rollback()  # Rollback the changes
        print(f"Duplicate key {index}")
        return
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

    time.sleep(random.uniform(0.1, 1))



def get_data_scraper2(url):
    t_st = time.time()
    response = requests.get(url)

    data = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        trs = soup.find_all("tr", class_="s1tfp426")
        for tr in trs:
            tds = tr.find_all("td")
            if len(tds) >= 2:
                td1 = str(tds[0].text).strip()
                td2 = str(tds[1].text).strip()
                data.append((td1, td2))
    else:
        print(f"ERROR::{response.status_code=}")

    t_res = round(time.time() - t_st, 2)
    return t_res, data, response.status_code


def scraper2(building_id, building_url):
    url = f"https://korter.kz{building_url}"
    try:
        t_exec, data, status_code = get_data_scraper2(url)
        print(f"{url=} :: {t_exec=}")

        if status_code in [500, 504]:
            not_processed_scraper2.append(building_id)
            return

        if len(data) > 0:
            print(f"[DATA]    :: {building_id=:<5} :: {building_url=:<50} :: {t_exec=}")
            db_srv.save_building_info_test(building_id, data)
        else:
            print(f"[NO_DATA] :: {building_id=:<5} :: {building_url=:<50} :: {t_exec=}")

    except requests.exceptions.ConnectionError:
        time.sleep(5)
        scraper2(building_id, building_url) 
    
    time.sleep(random.uniform(0.1, 1))

def scraper_full(not_processed_scraper1, not_processed_scraper2):
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(scraper1, range(3000, 3200))#runs 3 threads with scraper1 async
    
    print(f'\n\n\n{not_processed_scraper1=}')

    buildings_info = db_srv.get_buildings_without_full_info_test()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(scraper2, building_id, building_url): (building_id, building_url) for building_id, building_url in buildings_info}#runs 3 threads with scraper2 for each bid&burl in binfo async

        for future in concurrent.futures.as_completed(futures):#for error handling
            building_id, building_url = futures[future]
            try:
                future.result()#if exception is raised during scraper2 raises it here again to catch
            except Exception as e:
                print(f"Exception for building_id={building_id}, building_url={building_url}: {e}")

    print(f'\n\n\n{not_processed_scraper2=}')

if __name__ == "__main__":

    not_processed_scraper1 = []
    not_processed_scraper2 = []

    schedule.every().day.at("14:40").do(scraper_full, not_processed_scraper1, not_processed_scraper2)

    while True:
        schedule.run_pending()
        time.sleep(1)