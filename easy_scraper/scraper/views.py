from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

import requests
from bs4 import BeautifulSoup

from .models import Link


# can bring up to speed later
def scrape_home(req):
    if req.method == "POST":
        # grabbing non-validated/clean input with a default value of ''
        site = req.POST.get('site')
        default_url = 'https://www.google.com'
        if site == '':
            site = default_url

        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
        all_link_tags = soup.find_all('a')
        all_links = []
        # all_links.append(link_tag.get('href'))

        # no validation
        for link_tag in all_link_tags:
            address = link_tag.get('href')
            text = link_tag.string
            if text is None:
                text = 'placeholder title'
            print('here is text', text)
            Link.objects.create(address=address, link_name=text)
        return HttpResponseRedirect(reverse('home'))
    else:
        data = Link.objects.all()

    return render(req, 'scraper/home.html', {'data': data})


def clear_links(req):
    Link.objects.all().delete()
    return HttpResponseRedirect(reverse('home'))
    # return render(req, 'scraper/home.html')