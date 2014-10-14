import re

def find_status_detail(data):

    status_detail = []
    for match in re.findall('>(.*?)<', data):
        status_detail.append(match)

    return status_detail[:-1]
