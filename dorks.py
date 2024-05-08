"""
GOOGLE DORKS - напишите название сайта и сформируються OSINT данные
исспользованые самые популярные гугл дорки, которые помогают в разведке
тут будут размещены только самые популярные варианты, без воды
пример: ввели адресс сайта, потом открылы в гугл браузере
"""
def generate_google_search_link(site, query_type='email'):
    if query_type == 'email':
        search_query = f'site:{site} intext:e-mail'
    elif query_type == 'link:':
        search_query = f'link:{site}'
    elif query_type == 'pdf':
        search_query = f'site:{site} filetype:pdf'
    elif query_type == 'login':
        search_query = f'site:{site} inurl:login'
    encoded_query = '+'.join(search_query.split())
    google_link = f'https://www.google.com/search?q={encoded_query}'
    return google_link

if __name__ == "__main__":
    site = input("Введите сайт: ")
    google_links = []

    # Генерация наших ссылок
    google_links.append(generate_google_search_link(site, query_type='email'))
    google_links.append(generate_google_search_link(site, query_type='link:'))
    google_links.append(generate_google_search_link(site, query_type='pdf'))
    google_links.append(generate_google_search_link(site, query_type='login'))

    print("Дорки отображаеммые в Google:")
    for link in google_links:
        print(link)

#вывод robots.txt для возможного нахождения админки
def add_robots_txt(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url  # Можно также улучшить это, чтобы автоматически добавлялся префикс 'https://' в случае возможности
    if url.endswith('/'):
        url += 'robots.txt'
    else:
        url += '/robots.txt'
    return url

input_url = input("Введите адрес сайта: ")
final_url = add_robots_txt(input_url)
print("Ссылка на robots.txt: <a href='{}'>{}</a>".format(final_url, final_url))
