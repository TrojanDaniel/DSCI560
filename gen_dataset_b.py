

import json
import matplotlib.pyplot as plt

file_1=open('dataset_a.json','r')
rand_nums=file_1.read()
rand_nums_list=json.loads(rand_nums)
b_1=[i*3+6 for i in rand_nums_list]
print(b_1)
plt.title('visualization_b')
plt.scatter(range(len(b_1)),b_1,c='c',s=10)
plt.show()
json_b1=json.dumps(b_1)
file_b=open('dataset_b.json','w')
file_b.write(json_b1)
file_b.close()
