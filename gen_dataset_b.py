

import json

file_1=open('dataset_a.json','r')
rand_nums=file_1.read()
rand_nums_list=json.loads(rand_nums)
b_1=[i*3+6 for i in rand_nums_list]
json_b1=json.dumps(b_1)
file_b=open('dataset_b.json','w')
file_b.write(json_b1)
file_b.close()
