

import json
import matplotlib.pyplot as plt

file_1=open('1_a.json','r')
rand_nums=file_1.read()
rand_nums_x=json.loads(rand_nums)

file_2=open('1_b.json','r')
rand_nums_y=file_2.read()
rand_nums_y=json.loads(rand_nums_y)

x = rand_nums_x
y = rand_nums_y

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_title('Results')
plt.xlabel('X')
plt.ylabel('Y')
ax1.scatter(x,y,c = 'b',marker = 'o',s=0.2)
plt.legend('x1')
plt.savefig('results.png')
plt.show()