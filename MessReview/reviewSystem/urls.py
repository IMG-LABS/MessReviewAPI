from django.conf.urls import patterns, include, url
#from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from reviewSystem import views

urlpatterns = patterns('',
	url(r'^item/$', views.ItemDetails.as_view()),
	url(r'^item/(?P<pk>\d+)/$', views.ItemEdit.as_view()),#named group , passing variables from url to view
	url(r'^category$', views.CategoryDetails.as_view()),
	url(r'^user$', views.UserDetails.as_view()),
	url(r'^user/(?P<pk>\d+)/$', views.UserEdit.as_view()),
    #url(r'^$', views.hello, name='hello'),
)

urlpatterns = format_suffix_patterns(urlpatterns)

	