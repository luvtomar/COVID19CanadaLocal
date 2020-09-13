from django.conf.urls import url

from dashboard import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^sources$', views.sources, name='sources'),
    url(r'^(?P<current_city>[\s\S]*)/(?P<type>[\s\S]*)/$', views.LineChartJSONView.as_view(), name='line_chart_json')
]
