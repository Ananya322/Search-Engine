from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs


def index(request):
    return render(request, 'index3.html')


def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        url = 'https://www.google.com/search?q='+search
        res = requests.get(url)
        soup = bs(res.text, 'lxml')

        result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item'})

        final_result = []

        for result in result_listings:
            result_title = result.find(class_='PartialSearchResults-item-title').text
            result_url = result.find('a').get('href')
            result_desc = result.find(class_='PartialSearchResults-item-abstract').text

            final_result.append((result_title, result_url, result_desc))

        context = {
            'final_result': final_result
        }

        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')

