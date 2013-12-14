from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
import facebook


def get_last_status_message(graph_object, page_id):

    all_posts = graph_object.get_connections(id=page_id, connection_name='posts')
    list_of_posts = all_posts['data']
    list_of_posts.sort(key=lambda x: x['created_time'], reverse=True)
    status_message = list_of_posts[0]  # First Message on the list - with the latest date
    return status_message


# Create your views here.
def index(request):
    token = 'CAACEdEose0cBAHrmTnLQq3Wc5OPPEbeapFRUcSfNp1nHwKSbawDQaHZByq9UHiFyB3Uv1RNfxsQxCEKu0pRC76nKutDKyxER3Dx4P97pYEBZAZCLKOH8ZCEs8MU2IOkWwgWNUxB3MzB48NCYFf7GbtWvYKThUDBbuQGAGSXIUbpN6iLFD2z2ZAMDDC17WklYRvVV3sBI0RwZDZD'

    graph = facebook.GraphAPI(access_token=token)
    list_of_pages = ['naftalibennett', 'YairLapid', 'ShellyYachimovich']

    list_of_messages = [get_last_status_message(graph, page_id)['message'] for page_id in list_of_pages]

    context = {'list_of_messages': list_of_messages}
    return render(request, 'index.html', context)