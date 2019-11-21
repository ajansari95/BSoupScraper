import sys
import requests
import bs4
import re
from lxml import html

session_requests = requests.session()
initial_page = "https://bombayhighcourt.nic.in/case_query.php"
result = session_requests.get(initial_page)
tree = html.fromstring(result.text)

if len(sys.argv) == 3:
    url = sys.argv[1]
    file_name = sys.argv[2]

    print('Grabbing the page...')
    response = requests.get(url)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=re.compile('https://bombayhighcourt.nic.in/casequery_action.php?))

    file = open(file_name, 'wb')
    print('Collecting the links...')
    for link in links:
        href = link.get('href') + '\n'
        file.write(href.encode())
    file.close()
    print('Saved to %s' % file_name)
else:
    print('Usage: ./collect_links.py wwww.example.com file.txt')