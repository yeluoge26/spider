from requests_html import HTMLSession
from database import FormCsv

MAX_PAGE = 1000


def parse_page_videos(page_url):
    session = HTMLSession()
    r = session.get(page_url)
    print(page_url)
    # #main > div > div.main-content.main-category > div > div.movies-list.movies-list-full > div:nth-child(1) > a
    # #main > div > div.main-content.main-category > div > div.movies-list.movies-list-full > div:nth-child(1)
    # #main > div > div.main-content.main-category > div.movies-list.movies-list-full > div:nth-child(1)
    vids_html = r.html.find('div.movies-list.movies-list-full', first=True)
    vids = vids_html.find('a')
    page_result = []

    vtype = page_url.split('/')[-2]

    for v in vids:
        link = list(v.absolute_links)[0]
        title = v.attrs['title']
        c = v.find('img', first=True)
        cover = c.attrs['data-original']
        # print(cover)
        cover = cover.split('&url=')[-1]
        # print(link, title, cover)
        page_result.append({
            'title': title,
            'cover': cover,
            'link': link,
            'vtype': vtype
        })

    return page_result


def crawl_category_all_pages(categ_url, max_page=MAX_PAGE):
    form = FormCsv('output/page_index.csv', ['title', 'cover', 'link', 'vtype'])
    for i in range(1, max_page):
        page_url = categ_url + '/page-' + str(i)
        vids = parse_page_videos(page_url)
        if len(vids) == 0:
            break
        for vid in vids:
            form.save_row(vid)


def index_page(to_file='./output/category_javforme.txt'):
    with open(to_file, 'r') as f:
        categs = f.readlines()
        for categ in categs:
            url = categ.replace('\n', '')
            crawl_category_all_pages(url)


def main():
    # index_page()
    crawl_category_all_pages('http://javforme.me/category/uncensored')
    crawl_category_all_pages('http://javforme.me/japanese-porn-videos')


if __name__ == '__main__':
    main()
