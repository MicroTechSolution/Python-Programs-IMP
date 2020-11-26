'''import os
import platform
path_to_file = (r"E:\Roshanc\Desktop\offlineaadhaar20200927060401690.xml")
def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)

print(creation_date)'''

import os.path, time

file = (r"E:\Roshanc\Desktop\offlineaadhaar20200927060401690.xml")

print("last modified: %s" % time.ctime(os.path.getmtime(file)))
print("%s" % time.ctime(os.path.getctime(file)))
