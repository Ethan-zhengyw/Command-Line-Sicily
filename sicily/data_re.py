#-*- encoding: utf-8-*-
import re

def find_status_detail(data):

    status_detail = []
    for match in re.findall('>(.*?)<', data):
        if match != "":
            status_detail.append(match)

    return status_detail


def find_problem(data):
    problem = {}

    # in case of 10^7 become 107
    if "<sup>" in data:
        data = re.sub('<sup>(?P<sup>.*?)</sup>', '<sup>^\g<sup></sup>', data)

    patterns = {
        'id': '(?<=h1>)(\d+)\.\ (.*?)(?=<)',
        'title': '(?<=h1>)\d+\.\ (.*?)(?=<)',
        'time_limit': 'Time Limit:\ (.*?secs)',
        'memory_limit': 'Memory Limit:\ (.*?MB)'
    }

    for pattern in patterns:
        problem[pattern] = re.search(patterns[pattern], data).group(1)

    patterns2 = {
        'description': ['Description', 'Input'],
        'input': ['Input', 'Output'],
        'output': ['Output', 'Sample Input'],
        'sample_input': ['Sample Input', 'Sample Output'],
        'sample_output': ['Sample Output', '</html>']
    }

    patterns3 = {
        '&lt;': '<',
        '&rsquo;': "'",
        '&lsquo;': "'",
        '&quot;': '"',
        '&hellip;': '…',
        '&nbsp;': ' ',
        '&ndash;': '-'
    }

    for pattern in patterns2:
        problem[pattern] = ""
        start = data.find(patterns2[pattern][0] + '</h1>')
        end = data.find('<h1>' + patterns2[pattern][1])

        regexp = '>(.*?)<'
        if pattern in ["sample_input", "sample_output"]:
            regexp = 'pre>(.*?)<'

        for match in re.findall(regexp, data[start : end], re.S):
            if match not in ["", "\n", "\n                "]:
                for item in patterns3:
                    match = match.replace(item, patterns3[item])
                problem[pattern] += match

        if problem[pattern][-1] != "\n":
            problem[pattern] += "\n"

    return problem
