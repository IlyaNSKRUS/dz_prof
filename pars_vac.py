import bs4
from fake_headers import Headers
import requests
import json
import pprint

URL = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
# URL = 'https://novosibirsk.hh.ru/search/vacancy?text=Python&from=suggest_post&area=4&hhtmFrom=main&hhtmFromLabel=vacancy_search_line'

def get_headers():
    return Headers(browser='chrome', os='win').generate()

def find_vac():
    HEADERS = get_headers()
    main_responce = requests.get(url=URL, headers=HEADERS)
    main_html = main_responce.text
    soup = bs4.BeautifulSoup(main_html, 'lxml')
    main_tag_data = soup.find('div', id="a11y-main-content")
    vacancys = main_tag_data.find_all('div', class_="vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter")

    parsed_data = []

    for vacancy in vacancys:
        URL_vac = vacancy.find('a')['href']
        vac_responce = requests.get(url=URL_vac, headers=HEADERS)
        vac_html = vac_responce.text
        vac_soup = bs4.BeautifulSoup(vac_html, 'lxml')
        vac_content = vac_soup.find('div', class_='vacancy-section').text
        if 'Django' in vac_content or 'Flask' in vac_content:
            vac_location = json.loads(vac_soup.find('script', type="application/ld+json").text)['jobLocation']['address']['addressLocality']
            vac_company_name = vac_soup.find('span', class_="bloko-header-section-2 bloko-header-section-2_lite").text
            vac_cahs = vac_soup.find('span', class_='magritte-text___pbpft_3-0-11 magritte-text_style-primary___AQ7MW_3-0-11 magritte-text_typography-label-1-regular___pi3R-_3-0-11').text

            parsed_data.append(
                {"link": URL_vac, "vac_cahs": vac_cahs, "company_name": vac_company_name, "city": vac_location}
            )

        else:
            pass

    # pprint.pprint(parsed_data)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(parsed_data, file, ensure_ascii=False)

find_vac()