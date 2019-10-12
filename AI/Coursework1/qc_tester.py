## Test file for coursework 1

import sys,time
from tree          import *
from queue_search  import *
from queen_cover  import *

def zero_heuristic(state):
    return 0


start = time.time()

search(make_qc_problem(3,3), ('A_star', zero_heuristic), 5000, [])
search(make_qc_problem(4,4), ('A_star', zero_heuristic), 5000, [])
search(make_qc_problem(5,5), ('A_star', zero_heuristic), 5000, [])

search(make_qc_problem(5,6), ('A_star', zero_heuristic), 5000, [])
search(make_qc_problem(6,5), ('A_star', zero_heuristic), 5000, [])
search(make_qc_problem(10,3), ('A_star', zero_heuristic), 5000, [])

search(make_qc_problem(3,4), ('A_star', zero_heuristic), 5000, [])
search(make_qc_problem(4,7), ('A_star', zero_heuristic), 5000, [])
search(make_qc_problem(2,50), ('A_star', zero_heuristic), 5000, [])


print "\n\n\nRan All Tests Successfully in " + str(round(time.time()-start,2)) + " seconds\n\n\n"
# all tests run fine

# best time was 0.07
