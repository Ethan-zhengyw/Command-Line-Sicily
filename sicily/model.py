import urllib
import urllib2

header = {'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3','User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16'}

def req_login(id, pwd):

    data_login = urllib.urlencode ({
        'username': id,
        'password': pwd
    })

    req = urllib2.Request(
        url = 'http://soj.me/action.php?act=Login',
        data = data_login,
        headers = header
    )

    return req


def req_submit(problemID, sourceCode):

    data_submit = urllib.urlencode({
        'pid': problemID,
        'cid': '0',
        'language': '2',
        'source': sourceCode
    })

    req = urllib2.Request(
        url = 'http://soj.me/action.php?act=Submit',
        data = data_submit,
        headers = header
    )

    return req


def req_status(sid):

    data_query = urllib.urlencode({
        'sid': sid
    })

    req = urllib2.Request(
        url = 'http://soj.me/action.php?act=QueryStatus',
        data = data_query,
        headers = header
    )

    return req


def req_problem(problemID):

    req = urllib2.Request(
        url = 'http://soj.me/' + problemID,
        headers = header
    )

    return req
