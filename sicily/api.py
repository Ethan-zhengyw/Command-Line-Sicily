import urllib
import urllib2
import cookielib
import json
import re
import os
import model
import data_re

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def login():

    id, pwd = get_userInfo("soj.conf")
    result_login = opener.open(model.req_login(id, pwd))

    return ("1" in result_login.read())


def submit(problemID, sourceCode):

    result_submit = opener.open(model.req_submit(problemID, sourceCode))
    response = json.loads(result_submit.read())

    if response['success'] == 1:

        sid = response['sid']
        query_result = opener.open(model.req_status(sid)).read()

        print " Waiting..."
        while "Waiting" in query_result:
            query_result = opener.open(model.req_status(sid)).read()
        print " Judging..."
        while "Judging" in query_result:
            query_result = opener.open(model.req_status(sid)).read()
        print

        response = json.loads(query_result)
        if response["status"] == "Compile Error":
            response["status_detail"] = get_status_detail(response["sid"])

        return response


def get_status_detail(sid):

    req = model.req_status_detail(sid)
    result = opener.open(req)

    return data_re.find_status_detail(result.read())


def submit_sourceFile(problemID, filename):

    sourceFile = open(filename, "r")
    sourceCode = sourceFile.read()

    return submit(problemID, sourceCode)


def get_problem(problemID):

    data = opener.open(model.req_problem(problemID)).read()

    print data
    

def display_problemInfo(problem):

    print " Problem Info"
    print "+----------------------------"
    print " [" + problem["title"] + "]"
    print " [" + problem["time_limit"] + "]",
    print " [" + problem["memory_limit"] + "]\n"


def display_result(result):

    print " Result"
    print "+----------------------------"
    print "    Run Memory:   [" + result["run_memory"] + "KB]"
    print "      Run Time:   [" + result["run_time"] + "secs]"
    print "        Status:  ",
    if result["status"] == "Accepted":
        print bcolors.OKGREEN + '\033[1m[' + result["status"] + ']' + bcolors.ENDC
    else:
        print bcolors.FAIL + '\033[1m[' + result["status"] + ']' + bcolors.ENDC
    if "status_detail" in result:
        print " Error details:   \n"
        for line in result["status_detail"]:
            print "\t" + bcolors.WARNING + line + "!" + bcolors.ENDC


def get_userInfo(userconf):

    confstream = open(userconf, "r").read()
    regexp_id = '(?<=USERNAME).*?\[(.*?)]'
    regexp_pwd = '(?<=PASSWORD).*?\[(.*?)]'

    id = re.search(regexp_id, confstream).group(1)
    pwd = re.search(regexp_pwd, confstream).group(1)

    return id, pwd


#problem = get_problem("1150")
#for key in problem:
#    print key, problem[key]
