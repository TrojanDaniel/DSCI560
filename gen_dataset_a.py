
# author  Dongsheng Yang
# date  09/23/20

import random
import json

random_num=[random.randint(0,100) for i in range(1000)]
print(random_num)
a_1= json.dumps(random_num)
file_a= open('dataset_a.json', 'w')
file_a.write(a_1)
file_a.close()