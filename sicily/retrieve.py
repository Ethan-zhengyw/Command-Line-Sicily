import sys
import api

if __name__ == '__main__':

    api.login()

    if len(sys.argv) != 2:
        print 'Query problem using [python retrieve.py ProblemID]'
        exit(-1)

    problemID = sys.argv[1]

    problem = api.get_problem(problemID)
    api.display_problemInfo_detail(problem)
