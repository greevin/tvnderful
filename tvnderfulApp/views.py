from django.shortcuts import render
import requests
from datetime import datetime

def series_list(request):
    url = 'http://api.tvmaze.com/singlesearch/shows?q=elementary&embed=episodes'
    r = requests.get(url)

    response_dict = r.json()

    series_id = response_dict['id']
    series_name = response_dict['name']
    series_summary = response_dict['summary']
    series_network = response_dict['network']['name']
    series_episode = response_dict['_embedded']['episodes']

    return render(request, 'series-list.html',
                  {
                      'series_id': series_id,
                      'series_name': series_name,
                      'series_summary': series_summary,
                      'series_network': series_network,
                      'series_episode': series_episode,
                  })


def episode_detail(request, id):

    url = 'http://api.tvmaze.com/episodes/' + str(id)
    r = requests.get(url)

    response_dict = r.json()

    episode_name = response_dict['name']
    episode_season = response_dict['season']
    episode_number = response_dict['number']
    episode_airdate = response_dict['airdate']
    episode_summary = response_dict['summary']
    episode_image = response_dict['image']['medium']

    return render(request, 'episode-detail.html',
                  {
                      'episode_name': episode_name,
                      'episode_season': episode_season,
                      'episode_number': episode_number,
                      'episode_airdate': episode_airdate,
                      'episode_summary': episode_summary,
                      'episode_image': episode_image
                  })
