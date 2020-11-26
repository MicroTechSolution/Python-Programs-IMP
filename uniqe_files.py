#import datetime
#uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.')
#import ufp.path
#ufp.path.unique('./test.ext')
import random
random_string = "AOD" + str(random.randint(1000001, 9000001))
print(random_string)
f = open(random_string+'_'+"aadhar.txt", "w")
f.close()
