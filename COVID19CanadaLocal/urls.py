from django.conf.urls import url

from dashboard import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<current_city>[\w\s.@+-]+)/(?P<type>[\w\s.@+-]+)/$', views.LineChartJSONView.as_view(), name='line_chart_json')
]
