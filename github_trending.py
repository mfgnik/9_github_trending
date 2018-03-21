import requests
from datetime import datetime, timedelta
from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument(
        '--top_size',
        type=int,
        help='amount of repositories to find',
        default=20
    )
    parser.add_argument(
        '--days',
        type=int,
        help='how long ago could repository be created',
        default=7
    )
    return parser.parse_args()


def get_trending_repositories(top_size=20, days_ago=7):
    since_date_dt = datetime.now().date() - timedelta(days=days_ago)
    url = 'https://api.github.com/search/repositories'
    response = requests.get(
        url=url,
        params={
            'q': 'created:>{since_date}'.format(
                since_date=since_date_dt.strftime('%Y-%m-%d')),
            'sort': 'stars',

        }
    )
    return response.json()['items'][:top_size]


def print_repository_info(place, repository):
    print(50 * '-')
    print('Place of repository:', place)
    print('Name of repository:', repository['name'])
    print('Url of repository:', repository['url'])
    print('Amount of open issues:', repository['open_issues_count'])


if __name__ == '__main__':
    arguments = parse_arguments()
    trending_repositories = get_trending_repositories(
        arguments.top_size,
        arguments.days
    )
    for place, repository in enumerate(trending_repositories, start=1):
        print_repository_info(place, repository)
