from django.conf.urls import url

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),

]
