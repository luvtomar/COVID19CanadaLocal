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
#client = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = client["COVID19_Canada"]
client = pymongo.MongoClient('mongodb+srv://'+urllib.parse.quote('luvtomar')+':'+urllib.parse.quote('Maiden1@Tomar')+'@cluster0-osg1l.mongodb.net/test?retryWrites=true&w=majority')


case_records_db = client["COVID19_Canada"]
#print('number of collections - '+str(len(case_records_db.list_collection_names())))
latest_collection_date_string = max(sorted([dateTimeSort(date) for date in case_records_db.list_collection_names()])).strftime('%Y-%m-%d')

records_as_lists = []
IDs = []
cols = ['ID','City','Province','Date','Provincial Case or Repatriated Canadian Case ID','Sex','Age','Source','Details']
#cols = ['ID','Provincial Case or Repatriated Canadian Case ID','Date','Sex','Age','City','Province','Source','Details']
for document in case_records_db[latest_collection_date_string].find():
    for key in document:
        if type(document[key]) != list: continue #no need for the document id
        records_as_lists = []
        IDs = []
        time_string = str(key)
        date_time_string = latest_collection_date_string + ' ' + time_string
        #doc_datetime = datetime.strptime(date_time_string, '%Y/%m/%d %H:%M:%S')
        #print(len(document[key]))
        for record in document[key]:
            if int(record["ID"]) in IDs: continue
            IDs.append(int(record["ID"]))
            records_as_lists.append([int(record["ID"])]+list(record.values())[1:])
        break

covid19_df = pd.DataFrame(records_as_lists,columns=cols)


death_records_db = client["COVID19_Canada_deaths"]
#print('number of collections - '+str(len(case_records_db.list_collection_names())))
latest_death_collection_date_string = max(sorted([dateTimeSort(date) for date in death_records_db.list_collection_names()])).strftime('%Y-%m-%d')

deaths_as_lists = []
death_IDs = []
death_cols = ['ID','Region','Province','Date','Sex','Age']
#cols = ['ID','Provincial Case or Repatriated Canadian Case ID','Date','Sex','Age','City','Province','Source','Details']
for document in death_records_db[latest_death_collection_date_string].find():
    for key in document:
        if type(document[key]) != list: continue #no need for the document id
        deaths_as_lists = []
        death_IDs = []
        time_string = str(key)
        date_time_string = latest_death_collection_date_string + ' ' + time_string
        #doc_datetime = datetime.strptime(date_time_string, '%Y/%m/%d %H:%M:%S')
        #print(len(document[key]))
        for record in document[key]:
            if int(record["ID"]) in death_IDs: continue
            death_IDs.append(int(record["ID"]))
            deaths_as_lists.append([int(record["ID"])]+list(record.values())[1:])
        break

covid19_deaths_df = pd.DataFrame(deaths_as_lists,columns=death_cols)



def home(request):
    print(os.getcwd())
    print(os.listdir())
    os.chdir('/home/COVID19CanadaLocal/staticfiles')
    print(os.getcwd())
    print(os.listdir())
    cities = sorted(list(covid19_df["City"].unique()))
    if request.method == 'POST':
        current_city = request.POST['selected city']
        return render(request, 'home.html', {'cities': cities, 'current_city': current_city})
    return render(request, 'home.html', {'cities': cities, 'current_city': 'no city selected'})

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        if self.kwargs['type'] == 'cases':
            date_values = sorted([dateTimeSort(date) for date in list(covid19_df[covid19_df["City"] == self.kwargs['current_city']]["Date"].unique())])
        elif self.kwargs['type'] == 'deaths':
            date_values = sorted([dateTimeSort(date) for date in list(covid19_deaths_df[covid19_deaths_df["Region"] == self.kwargs['current_city']]["Date"].unique())])
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
            daily_count_values = list(covid19_df[covid19_df['City']==self.kwargs['current_city']].groupby('Date')['ID'].count())
            print('cases - ' + str(daily_count_values))
            for value in daily_count_values:
                total = total + value
                total_count_values.append(total)
        elif self.kwargs['type'] == 'deaths':
            daily_count_values = list(covid19_deaths_df[covid19_deaths_df['Region']==self.kwargs['current_city']].groupby('Date')['ID'].count())
            print('deaths - ' + str(daily_count_values))
            for value in daily_count_values:
                total = total + value
                total_count_values.append(total)
        return [daily_count_values, total_count_values]
    
#line_chart = TemplateView.as_view(template_name='line_chart.html')
#line_chart_json = LineChartJSONView.as_view()

