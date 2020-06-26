import re
import requests
import json
import urllib.parse

from os import system, name
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

# Define variables
url_course = 'https://igsyv1z1xi-2.algolianet.com/1/indexes/*/queries'
get_parameters = {
    'x-algolia-agent': 'Algolia for JavaScript (4.0.3); Browser (lite); react (16.13.1); react-instantsearch (6.3.0); JS Helper (3.1.1)',
    'x-algolia-api-key': '448c9e20c867b4a3f602687b5ec33890',
    'x-algolia-application-id': 'IGSYV1Z1XI'
}
limit = 25
limitFacets = 300
totalCourse = 970
result = []


class Command(BaseCommand):
    help = "Crawl data from website"

    def handle(self, *args, **options):
        self.crawl()
        self.save()

    def crawl(self):
        length = 0
        levels = [
            {
                'name': 'Introductory',
                'limit': 950
            },
            {
                'name': 'Intermediate',
                'limit': 910
            },
            {
                'name': 'Advanced',
                'limit': 350
            }
        ]
        for level in levels:
            pageIndex = 1
            index = 0
            while index < level['limit']:
                courses = self.getCourse(pageIndex, level['name']).values()
                for course in courses:
                    self.clear()
                    print('Đang crawl ở mức level:', level['name'])
                    print('Đang crawl trang thứ', pageIndex)
                    print('Đã crawl', index, 'trong', level['limit'], 'khóa học của level:', level['name'])
                    print('Đã crawl tất cả', length, 'khóa học')
                    info = self.getDetailCourse(course['url'])
                    course.update(info)
                    result.append(course)
                    index = index + 1
                    length = length + 1
                pageIndex = pageIndex + 1
    
    def save(self):
        self.clear()
        print('Saving data to file: edx_data.json')
        json_data = json.dumps(result)
        file = open("../../../edx_data.json", "w")
        file.write(json_data)
        print('Save data to file success!')
        file.close()
    
    def clear(self):
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear') 

    def generatePostData(self, hitsPerPage=10, maxPerFacet=300, page=1, level=0):
        indexName = 'product'
        params = {
            'highlightPreTag': '<ais-highlight-0000000000>',
            'highlightPostTag': '</ais-highlight-0000000000>',
            'maxValuesPerFacet': maxPerFacet,
            'hitsPerPage': hitsPerPage,
            'query': '',
            'filters': 'product:Course',
            'facets': '["subject","partner","program_type","level","availability","language"]',
            'page': page,
            'tagFilters': ''
        }
        if (0 != level):
            params.update({'facetFilters': '[["level:'+ level +'"]]'})
        return {
            'indexName': indexName,
            'params': urllib.parse.urlencode(params)
        }


    def getCourse(self, pageIndex, level):
        query = urllib.parse.urlencode(get_parameters)
        raw_data = '{"requests":[' + json.dumps(self.generatePostData(hitsPerPage=limit, maxPerFacet=limitFacets, page=pageIndex, level=level)) + ']}'
        response = requests.post(url_course + '?' + query, data=raw_data)
        if (response.status_code == 400):
            print('Error 400!')
            return 0
        result = {}
        response_contents = json.loads(response.content)['results'][0]['hits']
        index = 0
        for hit in response_contents:
            soup = BeautifulSoup(hit['primary_description'], "html.parser")
            result[index] = {
                'name': hit['title'],
                'date': hit['active_run_start'],
                'language': hit['language'],
                'level': hit['level'],
                'description': soup.get_text().replace('\n', ' '),
                'subjects': hit['subject'],
                'url': hit['marketing_url']
            }
            index = index + 1
        return result


    def getDetailCourse(self, url):
        response = requests.get(url )
        if (400 == response.status_code):
            return 0
        soup = BeautifulSoup(response.content, "html.parser")
        elements = soup.findAll('div', {'class': 'col'})
        elements2 = soup.findAll('div', {'class': 'course-description'})
        elements3 = soup.findAll('div', {'class': 'course-description d-flex flex-column'})
        images = soup.findAll('div',{'class':'col-lg-5 p-1'})
        for div in images :
            if div.img:
                image=(div.img['src'])
        return {
            'length': elements[1].text,
            'effort': elements[3].text,
            'price': elements[5].text,
            'institution': elements[7].text,
            'about-course': elements2[0].text,
            'content-course': "" if not elements3 else elements3[0].text,
            'link-image':image        
        }
        
    