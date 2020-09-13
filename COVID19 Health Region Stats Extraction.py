import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
import pandas as pd
import pymongo
import urllib
from datetime import datetime
import pytz
utc_now = pytz.utc.localize(datetime.utcnow())
current_datetime = utc_now.astimezone(pytz.timezone('America/Toronto'))


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--window-size=100x100')
#chrome_options.add_argument("window-size=600,600")
#chrome_options.add_argument('--user-data-dir=/tmp/user-data')
#chrome_options.add_argument('--hide-scrollbars')
#chrome_options.add_argument('--enable-logging')
#chrome_options.add_argument('--log-level=0')
#chrome_options.add_argument('--v=99')
#chrome_options.add_argument('--single-process')
#chrome_options.add_argument('--data-path=/tmp/data-path')
chrome_options.add_argument('--ignore-certificate-errors')
#chrome_options.add_argument('--homedir=/tmp')
#chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

#Initialize the dictionary of health regions and COVID 19 cases and deaths
cases = {}

#Nova Scotia
browser.get('https://novascotia.ca/coronavirus/data/')
time.sleep(5)
cases['Northern NS']={}
cases['Northern NS']['Current Total Cases']=int(browser.find_element_by_id('northern_num').text.replace(',','').replace(' ','').replace('*',''))
cases['Eastern NS']={}
cases['Eastern NS']['Current Total Cases']=int(browser.find_element_by_id('eastern_num').text.replace(',','').replace(' ','').replace('*',''))
cases['Central NS']={}
cases['Central NS']['Current Total Cases']=int(browser.find_element_by_id('central_num').text.replace(',','').replace(' ','').replace('*',''))
cases['Western NS']={}
cases['Western NS']['Current Total Cases']=int(browser.find_element_by_id('western_num').text.replace(',','').replace(' ','').replace('*',''))


browser.get('https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Nova_Scotia')
cases['Northern NS']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[5].find_elements_by_tag_name('tr')[2].find_elements_by_tag_name('td')[4].text.replace(',','').replace(' ','').replace('*',''))
cases['Eastern NS']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[5].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[4].text.replace(',','').replace(' ','').replace('*',''))
cases['Central NS']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[5].find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[4].text.replace(',','').replace(' ','').replace('*',''))
cases['Western NS']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[5].find_elements_by_tag_name('tr')[3].find_elements_by_tag_name('td')[4].text.replace(',','').replace(' ','').replace('*',''))





#Manitoba
browser.get('https://experience.arcgis.com/experience/f55693e56018406ebbd08b3492e99771/')

#Winnipeg
cases['Winnipeg']={}
cases['Winnipeg']['Current Total Cases']=int(input('Manually enter the number of cases in Winnipeg\n'))
cases['Winnipeg']['Current Total Deaths']=int(input('Manually enter the number of deaths in Winnipeg\n'))



#Southern MB
cases['Southern MB']={}
cases['Southern MB']['Current Total Cases']=int(input('Manually enter the number of cases in Southern MB\n'))
cases['Southern MB']['Current Total Deaths']=int(input('Manually enter the number of deaths in Southern MB\n'))



#Prairie Mountain MB
cases['Prairie Mountain MB']={}
cases['Prairie Mountain MB']['Current Total Cases']=int(input('Manually enter the number of cases in Prairie Mountain MB\n'))
cases['Prairie Mountain MB']['Current Total Deaths']=int(input('Manually enter the number of deaths in Prairie Mountain MB\n'))



#Northern MB
cases['Northern MB']={}
cases['Northern MB']['Current Total Cases']=int(input('Manually enter the number of cases in Northern MB\n'))
cases['Northern MB']['Current Total Deaths']=int(input('Manually enter the number of deaths in Northern MB\n'))



#Interlake-Eastern
cases['Interlake-Eastern']={}
cases['Interlake-Eastern']['Current Total Cases']=int(input('Manually enter the number of cases in Interlake-Eastern\n'))
cases['Interlake-Eastern']['Current Total Deaths']=int(input('Manually enter the number of deaths in Interlake-Eastern\n'))





#Saskatchewan
browser.get('https://www.saskatchewan.ca/government/health-care-administration-and-provider-resources/treatment-procedures-and-guidelines/emerging-public-health-issues/2019-novel-coronavirus/cases-and-risk-of-covid-19-in-saskatchewan')

#Far North SK
cases['Far North SK']={}
cases['Far North SK']['Current Total Cases']=int(input('Manually enter the number of cases in Far North SK\n'))
cases['Far North SK']['Current Total Deaths']=int(input('Manually enter the number of deaths in Far North SK\n'))



#North SK
cases['North SK']={}
cases['North SK']['Current Total Cases']=int(input('Manually enter the number of cases in North SK\n'))
cases['North SK']['Current Total Deaths']=int(input('Manually enter the number of deaths in North SK\n'))



#Saskatoon
cases['Saskatoon']={}
cases['Saskatoon']['Current Total Cases']=int(input('Manually enter the number of cases in Saskatoon\n'))
cases['Saskatoon']['Current Total Deaths']=int(input('Manually enter the number of deaths in Saskatoon\n'))



#Central SK
cases['Central SK']={}
cases['Central SK']['Current Total Cases']=int(input('Manually enter the number of cases in Central SK\n'))
cases['Central SK']['Current Total Deaths']=int(input('Manually enter the number of deaths in Central SK\n'))



#Regina
cases['Regina']={}
cases['Regina']['Current Total Cases']=int(input('Manually enter the number of cases in Regina\n'))
cases['Regina']['Current Total Deaths']=int(input('Manually enter the number of deaths in Regina\n'))



#South SK
cases['South SK']={}
cases['South SK']['Current Total Cases']=int(input('Manually enter the number of cases in South SK\n'))
cases['South SK']['Current Total Deaths']=int(input('Manually enter the number of deaths in South SK\n'))





#Ontario

#York Region Public Health Services
cases['York Region Public Health Services'] = {}
browser.get('https://ww4.yorkmaps.ca/COVID19/ProdDashboard/index.html')
cases['York Region Public Health Services']['Current Total Cases']=int(input('Manually enter the current total number of cases in York Region Public Health Services\n'))
cases['York Region Public Health Services']['Current Total Deaths']=int(input('Manually enter the current total number of deaths in York Region Public Health Services\n'))



#Windsor-Essex County Health Unit
cases['Windsor-Essex County Health Unit'] = {}
browser.get('https://www.wechu.org/cv/local-updates')
cases['Windsor-Essex County Health Unit']['Current Total Cases']=int(browser.find_elements_by_class_name('well')[1].text.split('\n')[1].replace('*','').replace(',',''))
cases['Windsor-Essex County Health Unit']['Current Total Deaths']=int(browser.find_elements_by_class_name('well')[2].text.split('\n')[1].replace('*','').replace(',',''))



#Wellington-Dufferin-Guelph Public Health
cases['Wellington-Dufferin-Guelph Public Health'] = {}
browser.get('https://app.powerbi.com/view?r=eyJrIjoiZjZhMjM5ZTAtMmVhNS00ODEwLWE1ZjUtMTJkNzVkMGZkODhmIiwidCI6IjA5Mjg0MzdlLTFhZTItNGJhNy1hZmQxLTY5NDhmY2I5MWM0OCJ9')
cases['Wellington-Dufferin-Guelph Public Health']['Current Total Cases']=int(input('Manually enter the current total number of cases in Wellington-Dufferin-Guelph Public Health\n'))
cases['Wellington-Dufferin-Guelph Public Health']['Current Total Deaths']=int(input('Manually enter the current total number of deaths in Wellington-Dufferin-Guelph Public Health\n'))



#Toronto Public Health
cases['Toronto Public Health'] = {}
browser.get('https://public.tableau.com/views/TorontoPublicHealth-COVID-19Summary/PublicDashboard?:showVizHome=no&:embed=true:device=desktop')
time.sleep(5)
cases['Toronto Public Health']['Current Total Cases']=int(browser.find_element_by_id('tabZoneId6').text.split('\n')[1].split(' ')[1].replace('*','').replace(',',''))
cases['Toronto Public Health']['Current Total Deaths']=int(browser.find_element_by_id('tabZoneId9').text.split('\n')[1].split(' ')[2].replace('*','').replace(',',''))



#Timiskaming Health Unit
cases['Timiskaming Health Unit'] = {}
browser.get('https://www.timiskaminghu.com/90484/covid-19#Epidemiology')
time.sleep(5)
cases['Timiskaming Health Unit']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[1].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text.replace('*','').replace(',',''))
#cases['Timiskaming Health Unit']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[3].text.replace('*','').replace(',',''))
cases['Timiskaming Health Unit']['Current Total Deaths']=int(input('Check for any updates on deaths in Timiskaming Health Unit, else, enter 0\n'))



#Thunder Bay District Health Unit
cases['Thunder Bay District Health Unit'] = {}
browser.get('https://www.tbdhu.com/status')
time.sleep(5)
cases['Thunder Bay District Health Unit']['Current Total Cases']=int(browser.find_elements_by_tag_name('p')[0].text.split(' ')[3].replace('*','').replace(',',''))
cases['Thunder Bay District Health Unit']['Current Total Deaths']=int(browser.find_elements_by_tag_name('p')[0].text.split(' ')[8].replace('*','').replace(',',''))



#Sudbury & District Health Unit
cases['Sudbury & District Health Unit'] = {}
browser.get('https://www.phsd.ca/health-topics-programs/diseases-infections/coronavirus/current-status-covid-19')
cases['Sudbury & District Health Unit']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[4].find_elements_by_tag_name('td')[1].text.replace('*','').replace(',',''))
cases['Sudbury & District Health Unit']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[6].find_elements_by_tag_name('td')[1].text.replace('*','').replace(',',''))



#Southwestern Public Health
cases['Southwestern Public Health'] = {}
browser.get('https://www.swpublichealth.ca/content/community-update-novel-coronavirus-covid-19')
cases['Southwestern Public Health']['Current Total Cases']=int(input('Manually enter the current total number of cases in Southwestern Public Health\n'))
cases['Southwestern Public Health']['Current Total Deaths']=int(input('Manually enter the current total number of deaths in Southwestern Public Health\n'))



#Simcoe Muskoka District Health Unit
cases['Simcoe Muskoka District Health Unit'] = {}
browser.get('https://datawrapper.dwcdn.net/oEk6V/29/')
cases['Simcoe Muskoka District Health Unit']['Current Total Cases']=int(browser.find_elements_by_tag_name('thead')[0].find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('th')[1].text.replace('*','').replace(',',''))
cases['Simcoe Muskoka District Health Unit']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[5].find_elements_by_tag_name('td')[1].text.replace('*','').replace(',',''))



#Renfrew County and District Health Unit
cases['Renfrew County and District Health Unit'] = {}
browser.get('https://www.rcdhu.com/novel-coronavirus-covid-19-2/')
cases['Renfrew County and District Health Unit']['Current Total Cases']=int(browser.find_elements_by_class_name('panel-body')[0].text.replace('*','').replace(',',''))
cases['Renfrew County and District Health Unit']['Current Total Deaths']=int(browser.find_elements_by_class_name('panel-body')[2].text.replace('*','').replace(',',''))



#Region of Waterloo, Public Health
cases['Region of Waterloo, Public Health'] = {}
browser.get('https://www.regionofwaterloo.ca/en/health-and-wellness/positive-cases-in-waterloo-region.aspx')
cases['Region of Waterloo, Public Health']['Current Total Cases']=int(input('Manually enter the current total number of cases in Region of Waterloo, Public Health\n'))
cases['Region of Waterloo, Public Health']['Current Total Deaths']=int(input('Manually enter the current total number of deaths in Region of Waterloo, Public Health\n'))



#Porcupine Health Unit
cases['Porcupine Health Unit'] = {}
browser.get('http://www.porcupinehu.on.ca/en/your-health/infectious-diseases/novel-coronavirus/covid-cases/')
cases['Porcupine Health Unit']['Current Total Cases']=len(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr'))
cases['Porcupine Health Unit']['Current Total Deaths']=len(browser.find_elements_by_xpath('//td[contains(text(),"Deceased")]'))



#Peterborough Public Health
cases['Peterborough Public Health'] = {}
browser.get('https://www.peterboroughpublichealth.ca/your-health/diseases-infections-immunization/diseases-and-infections/novel-coronavirus-2019-ncov/local-covid-19-status/')
cases['Peterborough Public Health']['Current Total Cases']=int(browser.find_element_by_xpath('//p[contains(text(),"Confirmed positive")]').text.split('\n')[0].split(' ')[2].replace('*','').replace(',',''))
cases['Peterborough Public Health']['Current Total Deaths']=int(browser.find_element_by_xpath('//p[contains(text(),"Confirmed positive")]').text.split('\n')[2].split(' ')[2].replace('*','').replace(',',''))



#Peel Public Health
cases['Peel Public Health'] = {}
browser.get('https://www.peelregion.ca/coronavirus/case-status/')
cases['Peel Public Health']['Current Total Cases']=int(input('Manually enter the current total number of cases in Peel Public Health\n'))
cases['Peel Public Health']['Current Total Deaths']=int(input('Manually enter the current total number of deaths in Peel Public Health\n'))



#Ottawa Public Health
cases['Ottawa Public Health'] = {}
browser.get('https://www.ottawapublichealth.ca/en/reports-research-and-statistics/la-maladie-coronavirus-covid-19.aspx')
cases['Ottawa Public Health']['Current Total Cases']=int(browser.find_element_by_xpath('//li[contains(text(),"laboratory-confirmed cases, including")]').text.split(' laboratory-confirmed cases, including ')[0].replace('*','').replace(',',''))
cases['Ottawa Public Health']['Current Total Deaths']=int(browser.find_element_by_xpath('//li[contains(text(),"laboratory-confirmed cases, including")]').text.split(' laboratory-confirmed cases, including ')[1].split(' ')[0].replace('*','').replace(',',''))



#Northwestern Health Unit
cases['Northwestern Health Unit'] = {}
browser.get('https://www.nwhu.on.ca/covid19/Pages/regional-COVID-19-results.aspx')
time.sleep(5)
cases['Northwestern Health Unit']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[11].find_elements_by_tag_name('tr')[10].find_elements_by_tag_name('td')[0].text.replace('*','').replace(',',''))
#cases['Northwestern Health Unit']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[3].text.replace('*','').replace(',',''))
cases['Northwestern Health Unit']['Current Total Deaths']=int(input('Check for any updates on deaths in Northwestern Health Unit, else, enter 0\n'))


#North Bay Parry Sound District Health Unit
cases['North Bay Parry Sound District Health Unit'] = {}
browser.get('https://www.myhealthunit.ca/en/health-topics/coronavirus.asp')
cases['North Bay Parry Sound District Health Unit']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text.replace('*','').replace(',',''))
cases['North Bay Parry Sound District Health Unit']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[3].text.replace('*','').replace(',',''))



#Niagara Region Public Health Department
cases['Niagara Region Public Health Department'] = {}
browser.get('https://www.niagararegion.ca/health/covid-19/statistics.aspx')
cases['Niagara Region Public Health Department']['Current Total Cases']=int(input('Manually enter the current total number of cases in Niagara Region Public Health Department\n'))
cases['Niagara Region Public Health Department']['Current Total Deaths']=int(input('Manually enter the current total number of deaths in Niagara Region Public Health Department\n'))



#Middlesex-London Health Unit
cases['Middlesex-London Health Unit'] = {}
browser.get('https://www.healthunit.com/covid-19-cases-middlesex-london')
cases['Middlesex-London Health Unit']['Current Total Cases']=int(input('Manually enter the current total number of cases in Middlesex-London Health Unit\n'))
cases['Middlesex-London Health Unit']['Current Total Deaths']=int(input('Manually enter the current total number of deaths in Middlesex-London Health Unit\n'))



#Leeds, Grenville and Lanark Distric Health Unit
cases['Leeds, Grenville and Lanark District Health Unit'] = {}
browser.get('https://healthunit.org/for-professionals/hospitals-ltc-retirement-homes/outbreak-management-resources/outbreak-status-report/')
cases['Leeds, Grenville and Lanark District Health Unit']['Current Total Cases']=int(browser.find_element_by_xpath('//p[contains(text(), "deaths in Leeds, Grenville and Lanark.")]').text.split(' cases and ')[0].split(' ')[2].replace('*','').replace(',',''))
cases['Leeds, Grenville and Lanark District Health Unit']['Current Total Deaths']=int(browser.find_element_by_xpath('//p[contains(text(), "deaths in Leeds, Grenville and Lanark.")]').text.split(' cases and ')[1].split(' ')[0].replace('*','').replace(',',''))



#Lambton Public Health
cases['Lambton Public Health'] = {}
browser.get('https://lambtonpublichealth.ca/2019-novel-coronavirus/')
cases['Lambton Public Health']['Current Total Cases']=int(input('Manually enter the current total number of cases in Lambton Public Health\n'))
cases['Lambton Public Health']['Current Total Deaths']=int(input('Manually enter the current total number of deaths in Lambton Public Health\n'))



#Kingston, Frontenac and Lennox & Addington Public Health
cases['Kingston, Frontenac and Lennox & Addington Public Health'] = {}
browser.get('https://app.powerbi.com/view?r=eyJrIjoiNDBhZDhlMjMtMjUyMi00OWViLTgxNzUtY2M5N2I1MDlkNzM4IiwidCI6Ijk4M2JmOTVjLTAyNDYtNDg5My05MmI4LTgwMWJkNTEwYjRmYSJ9')
cases['Kingston, Frontenac and Lennox & Addington Public Health']['Current Total Cases']=int(input('Manually enter the current total number of cases in Kingston, Frontenac and Lennox & Addington Public Health\n'))
cases['Kingston, Frontenac and Lennox & Addington Public Health']['Current Total Deaths']=int(input('Manually enter the current total number of deaths in Kingston, Frontenac and Lennox & Addington Public Health\n'))



#Huron Perth District Health Unit
cases['Huron Perth District Health Unit'] = {}
browser.get('https://www.hpph.ca/en/health-matters/covid-19-in-huron-and-perth.aspx#')
cases['Huron Perth District Health Unit']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[4].find_elements_by_tag_name('td')[1].text.replace('*','').replace(',',''))
cases['Huron Perth District Health Unit']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[1].find_elements_by_tag_name('tr')[5].find_elements_by_tag_name('td')[1].text.replace('*','').replace(',',''))



#Hastings and Prince Edward Counties Health Unit
cases['Hastings and Prince Edward Counties Health Unit'] = {}
browser.get('https://hpepublichealth.ca/covid-19-cases/')
cases['Hastings and Prince Edward Counties Health Unit']['Current Total Cases']=int(input('Manually enter the current total number of cases in Hastings and Prince Edward Counties Health Unit\n'))
cases['Hastings and Prince Edward Counties Health Unit']['Current Total Deaths']=int(input('Manually enter the current total number of deaths in Hastings and Prince Edward Counties Health Unit\n'))



#Hamilton Public Health Services
cases['Hamilton Public Health Services'] = {}
browser.get('https://www.hamilton.ca/coronavirus/status-cases-in-hamilton')
cases['Hamilton Public Health Services']['Current Total Cases']=int(browser.find_element_by_xpath('//strong[contains(text(), "Number of total cases - ")]').text.split('\n')[0].split(' - ')[1].replace('*','').replace(',',''))
cases['Hamilton Public Health Services']['Current Total Deaths']=int(browser.find_element_by_xpath('//strong[contains(text(), "Number of total cases - ")]').text.split('\n')[3].split(' ')[4].replace('*','').replace(',',''))



#Halton Region Health Department
cases['Halton Region Health Department'] = {}
browser.get('https://www.halton.ca/For-Residents/New-Coronavirus')
cases['Halton Region Health Department']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[5].find_elements_by_tag_name('td')[1].text.replace('*','').replace(',',''))
cases['Halton Region Health Department']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[5].find_elements_by_tag_name('td')[4].text.replace('*','').replace(',',''))



#Haliburton, Kawartha, Pine Ridge District Health Unit
cases['Haliburton, Kawartha, Pine Ridge District Health Unit'] = {}
browser.get('https://www.hkpr.on.ca/')
cases['Haliburton, Kawartha, Pine Ridge District Health Unit']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[4].text.replace('*','').replace(',',''))
cases['Haliburton, Kawartha, Pine Ridge District Health Unit']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[5].find_elements_by_tag_name('td')[4].text.replace('*','').replace(',',''))



#Haldimand-Norfolk Health Unit
cases['Haldimand-Norfolk Health Unit'] = {}
browser.get('https://hnhu.org/health-topic/coronavirus-covid-19/')
cases['Haldimand-Norfolk Health Unit']['Current Total Cases']=int(browser.find_elements_by_xpath('//p[contains(text(),"Lab-confirmed")]')[1].text.split('  ')[1].replace('*','').replace(',',''))
cases['Haldimand-Norfolk Health Unit']['Current Total Deaths']=int(browser.find_element_by_xpath('//p[contains(text(),"Deaths")]').text.split('  ')[1].replace('*','').replace(',',''))



#Grey Bruce Health Unit
cases['Grey Bruce Health Unit'] = {}
file = requests.get('https://www.publichealthgreybruce.on.ca/Portals/0/Topics/InfectiousDiseases/COVID19/Situation%20Reports/May2020_Situation_Report.pdf')
open('C:/Users/Luv/AppData/Local/Programs/Python/Python37/GreyBruceHealthUnit.pdf','wb').write(file.content)
os.system("pdftotext GreyBruceHealthUnit.pdf GreyBruceHealthUnit.txt")
f=open('GreyBruceHealthUnit.txt','r')
text = f.read()
for line in text.split('\n'):
    if 'cases to date' in line:
        for sentence in line.split('  '):
            if 'cases to date' in sentence:
                cases['Grey Bruce Health Unit']['Current Total Cases']=int(sentence.split(' ')[0].replace('*','').replace(',',''))
            if sentence.endswith('deaths'):
                cases['Grey Bruce Health Unit']['Current Total Deaths']=int(sentence.split(' ')[0].replace('*','').replace(',',''))
        break


#Eastern Ontario Health Unit
cases['Eastern Ontario Health Unit'] = {}
browser.get('https://eohu.ca/en/covid/covid-19-status-update-for-eohu-region')
cases['Eastern Ontario Health Unit']['Current Total Cases']=int(browser.find_elements_by_class_name('card-text')[0].text.replace('*','').replace(',',''))
cases['Eastern Ontario Health Unit']['Current Total Deaths']=int(browser.find_elements_by_class_name('card-text')[2].text.replace('*','').replace(',',''))


#Durham Region Health Department
cases['Durham Region Health Department'] = {}
browser.get('https://app.powerbi.com/view?r=eyJrIjoiMjU2MmEzM2QtNDliNS00ZmIxLWI5MzYtOTU0NTI1YmU5MjQ2IiwidCI6IjUyZDdjOWMyLWQ1NDktNDFiNi05YjFmLTlkYTE5OGRjM2YxNiJ9')
cases['Durham Region Health Department']['Current Total Cases']=int(input('Manually enter the current total number of cases in Durham Health Region\n'))
cases['Durham Region Health Department']['Current Total Deaths']=int(input('Manually enter the current total number of deaths in Durham Health Region\n'))


#Algoma Public Health Unit
cases['Algoma Public Health Unit'] = {}
browser.get('http://www.algomapublichealth.com/disease-and-illness/infectious-diseases/novel-coronavirus/current-status-covid-19/')
cases['Algoma Public Health Unit']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text.replace('*','').replace(',',''))
cases['Algoma Public Health Unit']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[4].find_elements_by_tag_name('td')[1].text.replace('*','').replace(',',''))

#Brant County Health Unit
cases['Brant County Health Unit'] = {}
browser.get('https://www.bchu.org/ServicesWeProvide/InfectiousDiseases/Pages/coronavirus.aspx')
cases['Brant County Health Unit']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text.replace('*','').replace(',',''))
cases['Brant County Health Unit']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[5].text.replace('*','').replace(',',''))


#Chatham-Kent Health Unit
cases['Chatham-Kent Health Unit'] = {}
browser.get('https://ckphu.com/current-situation-in-chatham-kent/')
cases['Chatham-Kent Health Unit']['Current Total Cases']=int(browser.find_elements_by_xpath('//div[@class="x-row-inner"]')[0].find_elements_by_tag_name('div')[0].find_element_by_class_name('cs-ta-justify').text.replace('*','').replace(',',''))
cases['Chatham-Kent Health Unit']['Current Total Deaths']=int(browser.find_elements_by_xpath('//div[@class="x-row-inner"]')[0].find_elements_by_class_name('x-col')[2].find_element_by_class_name('cs-ta-justify').text.replace('*','').replace(',',''))





#Newfoundland & Labrador
browser.get('https://www.arcgis.com/apps/opsdashboard/index.html#/d531a6b1720e4a84a540d1f2ab273463')
time.sleep(5)

#Eastern NL
browser.find_element_by_id('ember44').click()
time.sleep(5)
cases['Eastern NL']={}
cases['Eastern NL']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Eastern NL']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[5].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Central NL
browser.find_element_by_id('ember48').click()
time.sleep(5)
cases['Central NL']={}
cases['Central NL']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[1].find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Central NL']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[1].find_elements_by_tag_name('tr')[5].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Western NL
browser.find_element_by_id('ember52').click()
time.sleep(5)
cases['Western NL']={}
cases['Western NL']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Western NL']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[5].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Labrador-Grenfell
browser.find_element_by_id('ember56').click()
time.sleep(5)
cases['Labrador-Grenfell']={}
cases['Labrador-Grenfell']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[3].find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Labrador-Grenfell']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[3].find_elements_by_tag_name('tr')[5].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))




#New Brunswick
browser.get('https://www2.gnb.ca/content/gnb/en/corporate/promo/covid-19/maps_graphs.html')

#Moncton
cases['Moncton']={}
cases['Moncton']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Saint John
cases['Saint John']={}
cases['Saint John']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Fredericton
cases['Fredericton']={}
cases['Fredericton']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[2].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Edmundston
cases['Edmundston']={}
cases['Edmundston']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[3].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Campellton
cases['Campellton']={}
cases['Campellton']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[4].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Bathurst
cases['Bathurst']={}
cases['Bathurst']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[5].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Miramichi
cases['Miramichi']={}
cases['Miramichi']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[6].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))





#Prince Edward Island
browser.get('https://www.princeedwardisland.ca/en/information/health-and-wellness/pei-covid-19-testing-data')

#Kings (PEI)
cases['Kings (PEI)']={}
cases['Kings (PEI)']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[1].find_elements_by_tag_name('tr')[11].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))

#Queens (PEI)
cases['Queens (PEI)']={}
cases['Queens (PEI)']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[1].find_elements_by_tag_name('tr')[12].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))

#Prince (PEI)
cases['Prince (PEI)']={}
cases['Prince (PEI)']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[1].find_elements_by_tag_name('tr')[13].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))





#Northwest Territories
browser.get('https://www.gov.nt.ca/covid-19/')
cases['Northwest Territories']={}
cases['Northwest Territories']['Current Total Cases']=int(browser.find_elements_by_class_name('views-field-field-covid-stat')[3].text.replace(',','').replace(' ','').replace('*',''))



#Nunavut
browser.get('https://gov.nu.ca/health/information/covid-19-novel-coronavirus')
cases['Nunavut']={}
cases['Nunavut']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[0].text.replace(',','').replace(' ','').replace('*',''))



#Yukon
browser.get('https://yukon.ca/covid-19')
cases['Yukon']={}
cases['Yukon']['Current Total Cases']=int(browser.find_elements_by_class_name('field-items')[0].text.split('\n')[2].split(' ')[2].replace(',','').replace(' ','').replace('*',''))




#British Columbia
browser.get('https://governmentofbc.maps.arcgis.com/apps/opsdashboard/index.html#/11bd9b0303c64373b5680df29e5b5914')
time.sleep(10)

#Fraser
cases['Fraser'] = {}
browser.find_elements_by_xpath('//*[contains(text(),"Fraser")]')[0].click()
time.sleep(2)
cases['Fraser']['Current Total Cases'] = int(browser.find_elements_by_class_name('responsive-text-label')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Fraser']['Current Total Deaths'] = int(browser.find_elements_by_class_name('responsive-text-label')[8].text.replace(',','').replace(' ','').replace('*',''))



#Interior BC
browser.refresh()
time.sleep(10)
cases['Interior BC'] = {}
browser.find_elements_by_xpath('//*[contains(text(),"Interior")]')[0].click()
time.sleep(2)
cases['Interior BC']['Current Total Cases'] = int(browser.find_elements_by_class_name('responsive-text-label')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Interior BC']['Current Total Deaths'] = int(browser.find_elements_by_class_name('responsive-text-label')[8].text.replace(',','').replace(' ','').replace('*',''))



#Northern BC
browser.refresh()
time.sleep(10)
cases['Northern BC'] = {}
browser.find_elements_by_xpath('//*[contains(text(),"Northern")]')[0].click()
time.sleep(2)
cases['Northern BC']['Current Total Cases'] = int(browser.find_elements_by_class_name('responsive-text-label')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Northern BC']['Current Total Deaths'] = int(browser.find_elements_by_class_name('responsive-text-label')[8].text.replace(',','').replace(' ','').replace('*',''))



#Vancouver Coastal
browser.refresh()
time.sleep(10)
browser.find_elements_by_xpath('//*[contains(text(),"Vancouver Coastal")]')[0].click()
time.sleep(2)
vancouver_coastal_cases = int(browser.find_elements_by_class_name('responsive-text-label')[1].text.replace(',','').replace(' ','').replace('*',''))
vancouver_coastal_deaths = int(browser.find_elements_by_class_name('responsive-text-label')[8].text.replace(',','').replace(' ','').replace('*',''))



#Vancouver Island
browser.refresh()
time.sleep(10)
browser.find_elements_by_xpath('//*[contains(text(),"Vancouver Island")]')[0].click()
time.sleep(2)
vancouver_island_cases = int(browser.find_elements_by_class_name('responsive-text-label')[1].text.replace(',','').replace(' ','').replace('*',''))
vancouver_island_deaths = int(browser.find_elements_by_class_name('responsive-text-label')[8].text.replace(',','').replace(' ','').replace('*',''))

cases['Vancouver'] = {}
cases['Vancouver']['Current Total Cases'] = vancouver_coastal_cases + vancouver_island_cases
cases['Vancouver']['Current Total Deaths'] = vancouver_coastal_deaths + vancouver_island_deaths



#Alberta
browser.get('https://www.alberta.ca/stats/covid-19-alberta-statistics.htm')
browser.find_element_by_xpath('//a[contains(text(),"Data export")]').click()
try:
    os.chdir('C:/Users/Luv/Downloads')
    os.remove('C:/Users/Luv/Downloads/covid19dataexport.csv')
    os.chdir('C:/Users/Luv/AppData/Local/Programs/Python/Python37')
except:
    print('File already removed\n')
time.sleep(5)
browser.find_element_by_xpath('//span[contains(text(),"CSV")]').click()
time.sleep(5)
alberta_covid = pd.read_csv('C:/Users/Luv/Downloads/covid19dataexport.csv')

#Unknown AB
cases['Unknown AB'] = {}
cases['Unknown AB']['Current Total Cases']=int(alberta_covid['Alberta Health Services Zone'][alberta_covid['Alberta Health Services Zone']=='Unknown'].count())
cases['Unknown AB']['Current Total Deaths']=int(alberta_covid['Alberta Health Services Zone'][alberta_covid['Alberta Health Services Zone']=='Unknown'][alberta_covid['Case status']=='Died'].count())



#South AB
cases['South AB'] = {}
cases['South AB']['Current Total Cases']=int(alberta_covid['Alberta Health Services Zone'][alberta_covid['Alberta Health Services Zone']=='South Zone'].count())
cases['South AB']['Current Total Deaths']=int(alberta_covid['Alberta Health Services Zone'][alberta_covid['Alberta Health Services Zone']=='South Zone'][alberta_covid['Case status']=='Died'].count())



#North AB
cases['North AB'] = {}
cases['North AB']['Current Total Cases']=int(alberta_covid['Alberta Health Services Zone'][alberta_covid['Alberta Health Services Zone']=='North Zone'].count())
cases['North AB']['Current Total Deaths']=int(alberta_covid['Alberta Health Services Zone'][alberta_covid['Alberta Health Services Zone']=='North Zone'][alberta_covid['Case status']=='Died'].count())



#Edmonton
cases['Edmonton'] = {}
cases['Edmonton']['Current Total Cases']=int(alberta_covid['Alberta Health Services Zone'][alberta_covid['Alberta Health Services Zone']=='Edmonton Zone'].count())
cases['Edmonton']['Current Total Deaths']=int(alberta_covid['Alberta Health Services Zone'][alberta_covid['Alberta Health Services Zone']=='Edmonton Zone'][alberta_covid['Case status']=='Died'].count())



#Central AB
cases['Central AB'] = {}
cases['Central AB']['Current Total Cases']=int(alberta_covid['Alberta Health Services Zone'][alberta_covid['Alberta Health Services Zone']=='Central Zone'].count())
cases['Central AB']['Current Total Deaths']=int(alberta_covid['Alberta Health Services Zone'][alberta_covid['Alberta Health Services Zone']=='Central Zone'][alberta_covid['Case status']=='Died'].count())



#Calgary
cases['Calgary'] = {}
cases['Calgary']['Current Total Cases']=int(alberta_covid['Alberta Health Services Zone'][alberta_covid['Alberta Health Services Zone']=='Calgary Zone'].count())
cases['Calgary']['Current Total Deaths']=int(alberta_covid['Alberta Health Services Zone'][alberta_covid['Alberta Health Services Zone']=='Calgary Zone'][alberta_covid['Case status']=='Died'].count())



#Quebec
browser.get('https://www.quebec.ca/en/health/health-issues/a-z/2019-coronavirus/situation-coronavirus-in-quebec/')

#Region to be determined
cases['Region to be determined'] = {}
cases['Region to be determined']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[19].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Region to be determined']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[19].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Outside Quebec
cases['Outside Quebec'] = {}
cases['Outside Quebec']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[18].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Outside Quebec']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[18].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Terres-Cries-de-la-Baie-James
cases['Terres-Cries-de-la-Baie-James'] = {}
cases['Terres-Cries-de-la-Baie-James']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[17].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Terres-Cries-de-la-Baie-James']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[17].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Nunavik
cases['Nunavik'] = {}
cases['Nunavik']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[16].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Nunavik']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[16].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Montérégie
cases['Montérégie'] = {}
cases['Montérégie']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[15].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Montérégie']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[15].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Laurentides
cases['Laurentides'] = {}
cases['Laurentides']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[14].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Laurentides']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[14].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Lanaudière
cases['Lanaudière'] = {}
cases['Lanaudière']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[13].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Lanaudière']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[13].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Laval
cases['Laval'] = {}
cases['Laval']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[12].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Laval']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[12].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Chaudière-Appalaches
cases['Chaudière-Appalaches'] = {}
cases['Chaudière-Appalaches']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[11].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Chaudière-Appalaches']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[11].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Gaspésie-Îles-de-la-Madeleine
cases['Gaspésie-Îles-de-la-Madeleine'] = {}
cases['Gaspésie-Îles-de-la-Madeleine']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[10].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Gaspésie-Îles-de-la-Madeleine']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[10].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Nord-du-Québec
cases['Nord-du-Québec'] = {}
cases['Nord-du-Québec']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[9].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Nord-du-Québec']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[9].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Côte-Nord
cases['Côte-Nord'] = {}
cases['Côte-Nord']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[8].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Côte-Nord']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[8].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Abitibi-Témiscamingue
cases['Abitibi-Témiscamingue'] = {}
cases['Abitibi-Témiscamingue']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[7].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Abitibi-Témiscamingue']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[7].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Outaouais
cases['Outaouais'] = {}
cases['Outaouais']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[6].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Outaouais']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[6].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Montréal
cases['Montréal'] = {}
cases['Montréal']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[5].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Montréal']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[5].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Estrie
cases['Estrie'] = {}
cases['Estrie']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[4].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Estrie']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[4].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Mauricie-et-Centre-du-Québec
cases['Mauricie-et-Centre-du-Québec'] = {}
cases['Mauricie-et-Centre-du-Québec']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[3].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Mauricie-et-Centre-du-Québec']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[3].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Capitale-Nationale
cases['Capitale-Nationale'] = {}
cases['Capitale-Nationale']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[2].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Capitale-Nationale']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[2].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Saguenay – Lac-Saint-Jean
cases['Saguenay – Lac-Saint-Jean'] = {}
cases['Saguenay – Lac-Saint-Jean']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Saguenay – Lac-Saint-Jean']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))



#Bas-Saint-Laurent
cases['Bas-Saint-Laurent'] = {}
cases['Bas-Saint-Laurent']['Current Total Cases']=int(browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))
cases['Bas-Saint-Laurent']['Current Total Deaths']=int(browser.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[1].text.replace(',','').replace(' ','').replace('*',''))




print(cases)


##Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
#client = pymongo.MongoClient('mongodb://<sample-user>:<password>@sample-cluster.node.us-east-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred')
client = pymongo.MongoClient('mongodb+srv://'+urllib.parse.quote('luvtomar')+':'+urllib.parse.quote('Maiden1@Tomar')+'@cluster0-osg1l.mongodb.net/test?retryWrites=true&w=majority')

local_records_db = client["COVID19_Canada_local"]

for collection in local_records_db.list_collection_names():
    current_numbers=local_records_db[collection].find()[0]['Numbers']
    try:
        current_numbers[current_datetime.strftime('%Y-%m-%d')] = cases[collection]['Current Total Cases']-sum(list(current_numbers.values()))
    except:
        continue
    print(collection)
    print(current_numbers[current_datetime.strftime('%Y-%m-%d')])
    myquery={"Numbers":local_records_db[collection].find()[0]['Numbers']}
    newvalues={"$set":{"Numbers":current_numbers}}
    local_records_db[collection].update_one(myquery,newvalues)


    print(current_datetime.strftime('%Y-%m-%d %H:%M:%S'))
    myquery={"Last Update":local_records_db[collection].find()[0]['Last Update']}
    newvalues={"$set":{"Last Update":current_datetime.strftime('%Y-%m-%d %H:%M:%S')}}
    local_records_db[collection].update_one(myquery,newvalues)

print('\n\n\n\n\n\n\n\n\n\n')
local_death_records_db = client["COVID19_Canada_local_deaths"]

for collection in local_death_records_db.list_collection_names():
    current_numbers=local_death_records_db[collection].find()[0]['Numbers']
    try:
        current_numbers[current_datetime.strftime('%Y-%m-%d')] = cases[collection]['Current Total Deaths']-sum(list(current_numbers.values()))
    except:
        continue
    if (collection == 'Winnipeg') or (collection == 'Southern MB') or (collection == 'Prairie Mountain MB') or (collection == 'Northern MB') or (collection == 'Interlake-Eastern') or (collection == 'North SK') or (collection == 'Central SK') or (collection == 'Far North SK') or (collection == 'Saskatoon') or (collection == 'South SK') or (collection == 'Regina'):
        current_numbers[current_datetime.strftime('%Y-%m-%d')] = 0
    print(collection)
    print(current_numbers[current_datetime.strftime('%Y-%m-%d')])
    myquery={"Numbers":local_death_records_db[collection].find()[0]['Numbers']}
    newvalues={"$set":{"Numbers":current_numbers}}
    local_death_records_db[collection].update_one(myquery,newvalues)


    print(current_datetime.strftime('%Y-%m-%d %H:%M:%S'))
    myquery={"Last Update":local_death_records_db[collection].find()[0]['Last Update']}
    newvalues={"$set":{"Last Update":current_datetime.strftime('%Y-%m-%d %H:%M:%S')}}
    local_death_records_db[collection].update_one(myquery,newvalues)

browser.close()
browser.quit()
