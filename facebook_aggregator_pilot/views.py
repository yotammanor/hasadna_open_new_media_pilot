from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
import facebook
from random import randrange


PAGES_OF_POLITICIANS = ['naftalibennett', 'YairLapid', 'ShellyYachimovich', 'barackobama']


def get_last_status_message(graph_object, page_id):

    all_posts = graph_object.get_connections(id=page_id, connection_name='posts', args={"limit": "20"})
    list_of_posts = all_posts['data']
    list_of_posts.sort(key=lambda x: x['created_time'], reverse=True)
    status_message = list_of_posts[0]  # First Message on the list - with the latest date
    return status_message


def get_random_status_message(graph_object, page_id):

    all_posts = graph_object.get_connections(id=page_id, connection_name='posts', args={"limit": "20"})
    list_of_posts = all_posts['data']
    list_of_posts.sort(key=lambda x: x['created_time'], reverse=True)
    status_message = list_of_posts[randrange(len(list_of_posts))]  # A random post from the list
    return status_message


def get_list_of_pages(number_of_pages):
    local_pages_of_politicians = PAGES_OF_POLITICIANS
    selected_list_of_pages = list()
    while len(selected_list_of_pages)<=number_of_pages:
        selected_list_of_pages.append(local_pages_of_politicians.pop(randrange(len(local_pages_of_politicians))))
    return selected_list_of_pages


# Create your views here.
def index(request):
    token = 'CAACEdEose0cBAJ1slET8JLburo1Xli3wwXuynK5ktBqn1WWWNUkCyjx9q7FVoO9ZCCHddpEAJi9cKewGoZCSiH7H4VwH941pZAiQlOxBaUjAPpZA4MWb3TsQcrYyBjwZA40hi2j0ISJGFvdFDIyTV2TuJ7nIo85D0KIWb4ASk9rlZBjNA9Bb2MErVUqEUA3Q4ZD'

    graph = facebook.GraphAPI(access_token=token)
    list_of_pages = get_list_of_pages(number_of_pages=3)

    list_of_messages = [get_random_status_message(graph, page_id) for page_id in list_of_pages]

    context = {'list_of_messages': list_of_messages}
    return render(request, 'index.html', context)