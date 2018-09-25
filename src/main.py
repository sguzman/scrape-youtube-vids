import bs4
import requests
import json


def json_pretty(js):
    print(json.dumps(js, indent=' ', separators={', ', ': '}))


def process_script(script):
    raw_split = script.text.split('\n')
    raw_json = raw_split[1].lstrip('    window["ytInitialData"] = ').rstrip(';')
    return json.loads(raw_json)


def select_script_tag(soup):
    for script in soup.findAll('script'):
        if script.text.startswith('\n    window["ytInitialData"]'):
            return script


def soup_channel(chan_serial):
    url = f'https://www.youtube.com/channel/{chan_serial}/videos'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/69.0.3497.100 Safari/537.36 '

    headers = {'User-Agent': user_agent}
    req = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(req.text, 'html.parser')
    return soup


def main():
    chan_serial = 'UC0rZoXAD5lxgBHMsjrGwWWQ'
    soup = soup_channel(chan_serial)
    script = select_script_tag(soup)
    json_data = process_script(script)
    json_pretty(json_data)


main()
