import os
from datetime import timedelta
from datetime import datetime
def list_recent_workfiles(recentDays = 1, workingPath='.'):
    recentTime = timedelta(days = int(recentDays))
    searchTime = datetime.now()

    for root, dirs, files in os.walk(workingPath):
        for file in files:
            accessTime = datetime.fromtimestamp(os.path.getatime(os.path.join(root, file)))
            t_delta = searchTime - accessTime
            if t_delta <= recentTime:
                print(accessTime, file)
'''
    dirs = os.listdir()
    for item in dirs:
        accessTime = datetime.fromtimestamp(os.path.getatime(item))
        t_delta = searchTime - accessTime
        if t_delta <= recentTime:
            print(item, accessTime)
'''
if __name__ == "__main__":
    import sys
    argv_num = len(sys.argv)
    print('received ' + str(argv_num) + ' arguments:')

    for arg in sys.argv:
        print('    '+arg)
    print('')

    if argv_num == 1:
        list_recent_workfiles()
    elif argv_num == 2:
        list_recent_workfiles(sys.argv[1])
    elif argv_num == 3:
        list_recent_workfiles(sys.argv[1], sys.argv[2])
    else:
        print('Warning: invalid argument number as ' + argv_num
			+ '. Please invoke with: [m]command [o]recentAccessDays [o]workingPath.')
'''recentDays = sys.argv[1]
    workingPath = os.getcwd()
    list_recent_workfiles(recentDays, workingPath)
'''
