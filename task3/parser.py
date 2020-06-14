import lxml.html as html
import pandas as pd
import requests
import tqdm


def parse_uik_page(region, tik, uik_url):
    page = requests.get(uik_url)
    tree = html.fromstring(page.text)
    title_table, uik_table = tree.xpath("//table[6]//table")

    uik_names = uik_table.xpath('tr[1]/td/nobr/text()')
    titles = [text.strip() for text in title_table.xpath("tr/td[2]//text()")][1:]

    result = {
        "УИК": uik_names,
        "ТИК": [tik] * len(uik_names),
        "Регион": [region] * len(uik_names),
    }

    uik_table = uik_table.xpath('tr')[1:]

    for row, title in zip(uik_table, titles):
        row = row.xpath("td//b/text()")
        if row:
            result[title] = map(int, row)

    return pd.DataFrame(result)


def get_links(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    return [(link.text, link.attrib["href"]) for link in tree.xpath("//nobr//a")]


def parse(root):
    tables = []
    for region, region_url in tqdm.tqdm(get_links(root)):
        for tik, tik_url in get_links(region_url):
            page = requests.get(tik_url)
            tree = html.fromstring(page.text)
            uik_url = tree.xpath("//table[2]//tr[2]//td//a")[0].attrib["href"]
            tables.append(parse_uik_page(region, tik, uik_url))
    return pd.concat(tables)
