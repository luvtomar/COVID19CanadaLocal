import os
from django.shortcuts import render
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
import pymongo
import urllib
from datetime import datetime

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
client = pymongo.MongoClient('mongodb+srv://'+urllib.parse.quote('luvtomar')+':'+urllib.parse.quote('Maiden1@Tomar')+'@cluster0-osg1l.mongodb.net/test?retryWrites=true&w=majority')

local_records_db = client["COVID19_Canada_local"]

local_death_records_db = client["COVID19_Canada_local_deaths"]


def home(request):
    cities = sorted(local_records_db.list_collection_names())
    if request.method == 'POST':
        current_city = request.POST['selected city']
        if current_city == '':
            return render(request, 'home.html', {'cities': cities, 'current_city': 'no city selected', 'error_message':'T'})
        latest_collection_date_string = local_records_db[current_city].find()[0]['Last Update']
        current_province = local_records_db[current_city].find()[0]['Province']
        latest_death_collection_date_string = local_death_records_db[current_city].find()[0]['Last Update']
        render_params={'cities': cities, 'current_city': current_city, 'error_message':'F', 'case_record_time': latest_collection_date_string, 'death_record_time': latest_death_collection_date_string, 'current_province':current_province}
        return render(request, 'home.html', render_params)
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
                 'Quebec':'https://www.quebec.ca/en/health/health-issues/a-z/2019-coronavirus/situation-coronavirus-in-quebec/',
                 'Saskatchewan':'https://www.saskatchewan.ca/government/health-care-administration-and-provider-resources/treatment-procedures-and-guidelines/emerging-public-health-issues/2019-novel-coronavirus/cases-and-risk-of-covid-19-in-saskatchewan',
                 'Yukon':'https://yukon.ca/covid-19',
                 'Prince Edward Island': 'https://www.princeedwardisland.ca/en/information/health-and-wellness/pei-covid-19-testing-data',
                 'Algoma Public Health Unit (Ontario)': "http://www.algomapublichealth.com/disease-and-illness/infectious-diseases/novel-coronavirus/current-status-covid-19/",
                 'Brant County Health Unit (Ontario)':'https://www.bchu.org/ServicesWeProvide/InfectiousDiseases/Pages/coronavirus.aspx',
                 'Chatham-Kent Health Unit (Ontario)':'https://ckphu.com/current-situation-in-chatham-kent/',
                 'Durham Region Health Department (Ontario)':'https://ckphu.com/current-situation-in-chatham-kent/',
                 'Eastern Ontario Health Unit (Ontario)':'https://eohu.ca/en/covid/covid-19-status-update-for-eohu-region',
                 'Grey Bruce Health Unit (Ontario)':'https://www.publichealthgreybruce.on.ca/COVID-19/Current-Number-of-Cases',
                 'Haldimand-Norfolk Health Unit (Ontario)':'https://hnhu.org/health-topic/coronavirus-covid-19/',
                 'Haliburton, Kawartha, Pine Ridge District Health Unit (Ontario)':'https://www.hkpr.on.ca/',
                 'Halton Region Health Department (Ontario)':'https://www.halton.ca/For-Residents/New-Coronavirus',
                 'Hamilton Public Health Services (Ontario)':'https://www.hamilton.ca/coronavirus/status-cases-in-hamilton',
                 'Hastings and Prince Edward Counties Health Unit (Ontario)':'https://hpepublichealth.ca/covid-19-cases/',
                 'Huron Perth District Health Unit (Ontario)':'https://www.hpph.ca/en/health-matters/covid-19-in-huron-and-perth.aspx#',
                 'Kingston, Frontenac and Lennox & Addington Public Health (Ontario)':'https://app.powerbi.com/view?r=eyJrIjoiNDBhZDhlMjMtMjUyMi00OWViLTgxNzUtY2M5N2I1MDlkNzM4IiwidCI6Ijk4M2JmOTVjLTAyNDYtNDg5My05MmI4LTgwMWJkNTEwYjRmYSJ9',
                 'Lambton Public Health (Ontario)':'https://lambtonpublichealth.ca/2019-novel-coronavirus/',
                 'Leeds, Grenville and Lanark District Health Unit (Ontario)':'https://healthunit.org/for-professionals/hospitals-ltc-retirement-homes/outbreak-management-resources/outbreak-status-report/',
                 'Middlesex-London Health Unit (Ontario)':'https://www.healthunit.com/covid-19-cases-middlesex-london',
                 'Niagara Region Public Health Department (Ontario)':'https://www.niagararegion.ca/health/covid-19/statistics.aspx',
                 'North Bay Parry Sound District Health Unit (Ontario)':'https://www.myhealthunit.ca/en/health-topics/coronavirus.asp',
                 'Northwestern Health Unit (Ontario)':'https://www.nwhu.on.ca/covid19/Pages/regional-COVID-19-results.aspx',
                 'Ottawa Public Health (Ontario)':'https://www.ottawapublichealth.ca/en/reports-research-and-statistics/la-maladie-coronavirus-covid-19.aspx',
                 'Peel Public Health (Ontario)':'https://www.peelregion.ca/coronavirus/case-status/',
                 'Peterborough Public Health (Ontario)':'https://www.peterboroughpublichealth.ca/your-health/diseases-infections-immunization/diseases-and-infections/novel-coronavirus-2019-ncov/local-covid-19-status/',
                 'Porcupine Health Unit (Ontario)':'http://www.porcupinehu.on.ca/en/your-health/infectious-diseases/novel-coronavirus/covid-cases/',
                 'Region of Waterloo, Public Health (Ontario)':'https://www.regionofwaterloo.ca/en/health-and-wellness/positive-cases-in-waterloo-region.aspx',
                 'Renfrew County and District Health Unit (Ontario)':'https://www.rcdhu.com/novel-coronavirus-covid-19-2/',
                 'Simcoe Muskoka District Health Unit (Ontario)':'https://datawrapper.dwcdn.net/oEk6V/29/',
                 'Southwestern Public Health (Ontario)':'https://www.swpublichealth.ca/content/community-update-novel-coronavirus-covid-19',
                 'Sudbury & District Health Unit (Ontario)':'https://www.phsd.ca/health-topics-programs/diseases-infections/coronavirus/current-status-covid-19',
                 'Thunder Bay District Health Unit (Ontario)':'https://www.tbdhu.com/status',
                 'Timiskaming Health Unit (Ontario)':'https://www.timiskaminghu.com/90484/covid-19#Epidemiology',
                 'Toronto Public Health (Ontario)':'https://public.tableau.com/views/TorontoPublicHealth-COVID-19Summary/PublicDashboard',
                 'Wellington-Dufferin-Guelph Public Health (Ontario)':'https://app.powerbi.com/view?r=eyJrIjoiZjZhMjM5ZTAtMmVhNS00ODEwLWE1ZjUtMTJkNzVkMGZkODhmIiwidCI6IjA5Mjg0MzdlLTFhZTItNGJhNy1hZmQxLTY5NDhmY2I5MWM0OCJ9',
                 'Windsor-Essex County Health Unit (Ontario)':'https://www.wechu.org/cv/local-updates',
                 'York Region Public Health Services (Ontario)':'https://ww4.yorkmaps.ca/COVID19/ProdDashboard/index.html'
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
