from django.conf.urls import patterns, include, url
from django.contrib import admin
#from reviewSystem.views import hello

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'messReview.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^reviewSystem/',include('reviewSystem.urls')), #for  API
    #url(r'^', include('reviewSystem.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
	