
# author  Dongsheng Yang
# date  09/23/20

import random
import json
import matplotlib.pyplot as plt
random_num=[random.randint(0,100) for i in range(1000)]
print(random_num)
plt.title('visualization_a')
plt.scatter(range(len(random_num)),random_num,c='c',s=10)
plt.show()
a_1= json.dumps(random_num)
file_a= open('dataset_a.json', 'w')
file_a.write(a_1)
file_a.close()