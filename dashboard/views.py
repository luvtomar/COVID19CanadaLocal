import os
from  django.shortcuts import render
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
import pymongo
import urllib
from datetime import datetime
import pandas as pd

def dateTimeSort(item):
    if '/' in item and ':' in item:
        return datetime.strptime(item, '%Y/%m/%d %H:%M:%S')
    elif '/' in item:
        return datetime.strptime(item, '%Y/%m/%d')
    elif '-' in item and ':' in item:
        return datetime.strptime(item, '%Y-%m-%d %H:%M:%S')
    elif '-' in item:
        return datetime.strptime(item, '%Y-%m-%d')
    return datetime.strptime(item, '%H:%M:%S')

##Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
#client = pymongo.MongoClient('mongodb://<sample-user>:<password>@sample-cluster.node.us-east-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred')
client = pymongo.MongoClient('mongodb+srv://'+urllib.parse.quote('luvtomar')+':'+urllib.parse.quote('MY-PASSWORD')+'@cluster0-osg1l.mongodb.net/test?retryWrites=true&w=majority')

local_records_db = client["COVID19_Canada_local"]

local_death_records_db = client["COVID19_Canada_local_deaths"]


def home(request):
    cities = sorted(local_records_db.list_collection_names())
    if request.method == 'POST':
        current_city = request.POST['selected city']
        if current_city == '':
            print('empty selection')
            return render(request, 'home.html', {'cities': cities, 'current_city': 'no city selected', 'error_message':'T'})
        latest_collection_date_string = local_records_db[current_city].find()[0]['Last Update']
        latest_death_collection_date_string = local_death_records_db[current_city].find()[0]['Last Update']
        return render(request, 'home.html', {'cities': cities, 'current_city': current_city, 'error_message':'F', 'case_record_time': latest_collection_date_string, 'death_record_time': latest_death_collection_date_string})
    return render(request, 'home.html', {'cities': cities, 'current_city': 'no city selected', 'error_message':'F'})


def sources(request):
    source_list={'Alberta':'https://covid19stats.alberta.ca/',
                 'British Columbia':'https://governmentofbc.maps.arcgis.com/apps/opsdashboard/index.html#/11bd9b0303c64373b5680df29e5b5914',
                 'Manitoba':'https://manitoba.maps.arcgis.com/apps/opsdashboard/index.html#/c7814c9d73e840f6be29c0ae0430c4bf',
                 'New Brunswick':'https://www2.gnb.ca/content/gnb/en/corporate/promo/covid-19/maps_graphs.html',
                 'Newfoundland and Labrador':'https://www.arcgis.com/apps/opsdashboard/index.html#/d531a6b1720e4a84a540d1f2ab273463',
                 'Northwest Territories':'https://www.hss.gov.nt.ca/en/services/coronavirus-disease-covid-19',
                 'Nova Scotia':'https://novascotia.ca/coronavirus/data/',
                 'Nunavut':'https://gov.nu.ca/health/information/covid-19-novel-coronavirus',
                 'Ontario':'https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv',
                 'Quebec':'https://www.quebec.ca/en/health/health-issues/a-z/2019-coronavirus/situation-coronavirus-in-quebec/',
                 'Saskatchewan':'https://www.saskatchewan.ca/government/health-care-administration-and-provider-resources/treatment-procedures-and-guidelines/emerging-public-health-issues/2019-novel-coronavirus/cases-and-risk-of-covid-19-in-saskatchewan',
                 'Yukon':'https://yukon.ca/covid-19'
                 }
    return render(request, 'sources.html',{'source_list':list(source_list.items())})


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        if self.kwargs['type'] == 'cases':
            date_values = sorted([dateTimeSort(date) for date in list(local_records_db[self.kwargs['current_city']].find()[0]['Numbers'].keys())])
        elif self.kwargs['type'] == 'deaths':
            date_values = sorted([dateTimeSort(date) for date in list(local_death_records_db[self.kwargs['current_city']].find()[0]['Numbers'].keys())])
        return [date_value.strftime('%Y-%m-%d') for date_value in date_values]
        #return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        if self.kwargs['type'] == 'cases':
            return ['Daily Number of Cases', 'Total Number of Cases']
        if self.kwargs['type'] == 'deaths':
            return ['Daily Number of Deaths', 'Total Number of Deaths']

    def get_data(self):
        """Return 3 datasets to plot."""
        daily_count_values = []
        total_count_values = []
        total = 0
        if self.kwargs['type'] == 'cases':
            date_values = sorted([dateTimeSort(date) for date in list(local_records_db[self.kwargs['current_city']].find()[0]['Numbers'].keys())])
            for date in date_values:
                daily_count_values.append(local_records_db[self.kwargs['current_city']].find()[0]['Numbers'][date.strftime('%Y-%m-%d')])
                total = total + local_records_db[self.kwargs['current_city']].find()[0]['Numbers'][date.strftime('%Y-%m-%d')]
                total_count_values.append(total)
            #daily_count_values = list(covid19_df[covid19_df['City']==self.kwargs['current_city']].groupby('Date')['ID'].count())
            #print('cases - ' + str(daily_count_values))
            #for value in daily_count_values:
            #    total = total + value
            #    total_count_values.append(total)
        elif self.kwargs['type'] == 'deaths':
            date_values = sorted([dateTimeSort(date) for date in list(local_death_records_db[self.kwargs['current_city']].find()[0]['Numbers'].keys())])
            for date in date_values:
                daily_count_values.append(local_death_records_db[self.kwargs['current_city']].find()[0]['Numbers'][date.strftime('%Y-%m-%d')])
                total = total + local_death_records_db[self.kwargs['current_city']].find()[0]['Numbers'][date.strftime('%Y-%m-%d')]
                total_count_values.append(total)
            #daily_count_values = list(covid19_deaths_df[covid19_deaths_df['Region']==self.kwargs['current_city']].groupby('Date')['ID'].count())
            #print('deaths - ' + str(daily_count_values))
            #for value in daily_count_values:
            #    total = total + value
            #    total_count_values.append(total)
        return [daily_count_values, total_count_values]
    
#line_chart = TemplateView.as_view(template_name='line_chart.html')
#line_chart_json = LineChartJSONView.as_view()

