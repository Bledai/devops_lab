import argparse
import requests
import getpass
import datetime


class CredentialsError(Exception):
    def __init__(self, txt):
        self.txt = txt
        print(self.txt)
        exit(0)


def parsArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', help='show the script version',
                        action='version',
                        version='version 1.0')

    parser.add_argument('-c', '--count', help='show count of pull requests',
                        action='store_true')

    parser.add_argument('--rate', help='show merged/closed statistics',
                        action='store_true')

    parser.add_argument('-n', '--numberPull', help='Set pull number')

    parser.add_argument('--open', help='Show who opened pull request/requests',
                        action='store_true')

    parser.add_argument('-d', '--date',
                        help='Days opened pull requesyt/requests', action='store_true')

    parser.add_argument('--comments',
                        help='Show the number of comments for pull request (required -p/--pull)',
                        action='store_true')

    parser.add_argument('--user', type=str, help='An owner of repository', required=True)

    parser.add_argument('-r', '--repository', type=str, help='A GitHub repository', required=True)
    args = parser.parse_args()
    return args


def getUrl(url, headers):
    try:
        pulls = requests.get(url, headers=headers).json()
        if pulls['message'] == 'Bad credentials':
            raise CredentialsError('Bad credentials: check token and try again')
        if pulls['message'] == 'Not Found':
            raise CredentialsError('Please check name and directory , try again')
    except (KeyError, TypeError):
        pass
    return pulls


def countPulls(url, headers):
    pulls = getUrl(url, headers)
    print('Count of pull requests: ', pulls[0]['number'])


def rateSt(url, headers):
    pulls = getUrl(url, headers)
    count = pulls[0]['number']
    merged = 0
    closed = 0
    for pull in pulls:
        if pull['merged_at']:
            merged += 1
        if pull['closed_at']:
            closed += 1
    print('Merged rate = {merged} / {count} \n'
          'Closed rate = {closed} / {count} '.format(merged=merged, closed=closed, count=count))


def whoOpened(url, headers, numberPull=None):

    if numberPull is not None:
        pull = getUrl(f'{url}/{numberPull}', headers)
        print('{user} opened pull {numberPull}'.format(user=pull["user"]["login"],
                                                       numberPull=numberPull))
    else:
        pulls = getUrl(url, headers)
        for pull in pulls:
            print('{user} opened pull {numberPull}'.format(user=pull["user"]["login"],
                                                           numberPull=pull['number']))


def countComments(url, headers):
    pulls = getUrl(url, headers)
    print('The pull has {lens} comment(s)'.format(lens=len(pulls)))


def dateInformation(url, headers, numberPull=None):
    if numberPull is not None:
        pull = getUrl(f'{url}/{numberPull}', headers)
        if pull['state'] == 'open':
            fullInform = pull['created_at'].split('T')
            a = fullInform[0].split('-')
            dateCteate = datetime.date(int(a[0]), int(a[1]), int(a[2]))
            dateToday = datetime.date.today()
            print('Days open: ', (dateToday - dateCteate).days, ' days',
                  '{user}:{numberPull}'.format(user=pull["user"]["login"],
                                               numberPull=pull['number']))
        else:
            print('Pull requsts closed')

    else:
        pulls = getUrl(url, headers)
        for pull in pulls:
            if pull['state'] == 'open':
                fullInform = pull['created_at'].split('T')
                a = fullInform[0].split('-')
                dateCteate = datetime.date(int(a[0]), int(a[1]), int(a[2]))
                dateToday = datetime.date.today()
                print('Days open: ', (dateToday - dateCteate).days, ' days',
                      '{user}:{numberPull}'.format(user=pull["user"]["login"],
                                                   numberPull=pull['number']))
            else:
                print('Pull requsts closed')


if __name__ == '__main__':
    args = parsArgs()
    token = getpass.getpass(prompt='Enter your asses token: ')
    url = f'https://api.github.com/repos/{args.user}/{args.repository}/pulls'
    headers = {'Authorization': 'token %s' % token}

    if args.count:
        countPulls(url, headers)

    if args.rate:
        rateSt(url, headers)

    if args.open:
        whoOpened(url, headers, args.numberPull)

    if args.numberPull and args.comments:
        countComments(f'{url}/{args.numberPull}/comments', headers)

    if args.date:
        dateInformation(url, headers, args.numberPull)
