from pyramid.view import view_config
import requests
import urllib2
from bs4 import BeautifulSoup
import csv
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.response import FileResponse

@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    return {'project': 'scrap'}


@view_config(route_name='content', renderer='templates/contents.jinja2')
def content(request):
    data_list = []
    url = ''
    url_valid = ''
    if request.method == "POST":
        url = request.POST['url']
        r = requests.get(url)
        print "ddddddddddddddd", r.status_code
        if r.status_code == 200:
            data = r.text
            soup = BeautifulSoup(data)
            try:
                for row in soup.find_all('div', attrs={"class": "toc"}):
                    for a in row.select('a'):
                        final_data = {'index': ''.join(a.text.split(' ')[0]).encode('utf-8'),
                                      'title': ''.join(a.text.split(' ')[1]),
                                      'href': url + str(a.attrs['href']).encode('utf-8')}
                        data_list.append(final_data)
            except Exception as e:
                pass
        else:
            url_valid = 'Not a Valid Wiki Url'
    return{'project': 'scrap', 'data': data_list, 'url': url.encode('utf-8'), 'url_valid': url_valid}
