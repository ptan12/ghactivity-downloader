import requests

def download_file(file):
    res = requests.get(f'https://data.gharchive.org/{file}')
    return res

# res= download_file('2021-01-01-0.json.gz')
# #res= download_file('2015-01-01-15.json.gz')
#
#
# print(res.status_code)
