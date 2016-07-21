import requests
import urllib2
from bs4 import BeautifulSoup
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.renderers import render_to_response


@view_config(route_name='home', renderer='templates/index.jinja2')
def hello_world(request):
    return dict()

    #return Response('Hello Vishnu')

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()



data_list = []
r = requests.get('https://en.wikipedia.org/wiki/Yahoo!')
data = r.text
soup = BeautifulSoup(data)
for row in soup.find_all('div',attrs={"class" : "toc"}):
    for a in row.select('a'):
        final_data = {'index': ''.join(a.text.split(' ')[0]).encode('utf-8'), 'title': ''.join(a.text.split(' ')[1]).encode('utf-8'), 'href': str(a.attrs['href']).encode('utf-8')}
	data_list.append(final_data)


print "d", data_list





