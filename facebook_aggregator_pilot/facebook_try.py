__author__ = 'yotam'

import facebook
from pprint import pprint
token = 'CAACEdEose0cBAAq1IEnXnZBPb72nMZB7FeySIst8oZCKR7OMiNZCpuzPLYVurQEsNVbZAXtIMx6HyDgW4YSE2ESJsGlKZCdXwaHFIU6WkIMopX7DUYvCe2cQtbfZBUfj61isPleDkrgr74HMDmuXZBfQWV1fXtvyywMmfSbcHIYGN1nhUgfndyYHjovtsQ4WStMZD'
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

