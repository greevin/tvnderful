from django.shortcuts import render
import requests


def series_list(request, id):
    # http://api.tvmaze.com/shows/1
    show_url = 'http://api.tvmaze.com/shows/' + str(id)
    episodes_url = 'http://api.tvmaze.com/shows/' + str(id) + '/episodes'
    show_info = requests.get(show_url)
    episodes_info = requests.get(episodes_url)

    show_dict = show_info.json()
    episodes_dict = episodes_info.json()

    series_id = show_dict['id']
    series_name = show_dict['name']
    series_summary = show_dict['summary']
    series_network = show_dict['network']['name']
    series_episode = episodes_dict

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

    if response_dict['image'] is None and episode_summary == '':
        episode_image = ''
        episode_summary = '<br>No summary'
    else:
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


def show_index(request):
    url = 'http://api.tvmaze.com/shows'
    r = requests.get(url)

    shows = r.json()

    return render(request, 'show-index.html', {'shows': shows})
