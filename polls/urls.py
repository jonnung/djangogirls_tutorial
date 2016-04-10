# -*- coding: utf8 -*-

from django.conf.urls import patterns, url
from polls import views

# URLConf 모듈을 계층적으로 구성하는 것이 변경도 쉬워지고, 확장이 용이해진다.
# mysite.urls 에 모든 패턴을 등록하면 나중에 패턴이 변경되었을 때 고쳐야할 부분이 많아진다.
# patterns 함수는 Deprecated, Django 1.10 에서 삭제될 예정
urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote')
)
