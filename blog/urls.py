from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^subPage$', views.subPage, name='subPage'),

    
    url(r'^cimage$', views.cimage, name='cimage'),
    
    
    
    
    
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

    # ex: /polls/5/
    url(r'^polls$', views.polls_index, name='polls_index'),
    # ex: /polls/5/
    url(r'^polls/(?P<question_id>\d+)/$', views.polls_detail, name='polls_detail'),
    # ex: /polls/5/results/
    url(r'^polls/(?P<question_id>\d+)/results/$', views.polls_results, name='polls_results'),
    # ex: /polls/5/vote/
    url(r'^polls/(?P<question_id>\d+)/vote/$', views.polls_vote, name='polls_vote'),       
]