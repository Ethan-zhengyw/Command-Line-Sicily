import sys
import api

if __name__ == '__main__':

    api.login()

    if len(sys.argv) != 3:
        print 'Submit code using [python main.py ProblemID Filename]'
        exit(-1)

    problemID = sys.argv[1]
    filename = sys.argv[2]

    #problem = api.get_problem(problemID)
    #api.display_problemInfo(problem)

    result = api.submit_sourceFile(problemID, filename)
    api.display_result(result)
