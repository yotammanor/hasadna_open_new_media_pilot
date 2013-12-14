from random import randrange

__author__ = 'yotam'

import facebook
from pprint import pprint
token = 'CAACEdEose0cBAEZAoiPZAaRLCu2NIPTyVEK9ZCQNbWSnkNoNUhmA0uuIbQZAD9v1lltnkjQ8EKp9uMJHunLUG5khhAkLOX8Pb1lKArHT5a1j9TDnIxlAczh2QZBhzw8rIIgZBbnqRgewWUbQdnFC7ML4z7x3e3bWoLxE3uDNsHb5lIwZCeyEnGC7SvqmFMjnrR7K5r4eBGRVQZDZD'
graph = facebook.GraphAPI(access_token=token)

profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

list_of_friends = [friend['name'] for friend in friends['data']]

pprint(len(list_of_friends))


def get_last_status_message(graph_object, page_id):

    all_posts = graph_object.get_connections(id=page_id, connection_name='posts')
    list_of_posts = all_posts['data']
    list_of_posts.sort(key=lambda x: x['created_time'], reverse=True)
    status_message = list_of_posts[0]  # First Message on the list - with the latest date
    return status_message


def get_random_status_message(graph_object, page_id):

    all_posts = graph_object.get_connections(id=page_id, connection_name='posts')
    list_of_posts = all_posts['data']
    list_of_posts.sort(key=lambda x: x['created_time'], reverse=True)
    status_message = list_of_posts[randrange(len(list_of_posts))]  # A random post from the list
    return status_message
