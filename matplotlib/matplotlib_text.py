import matplotlib.pyplot as plt

def figure():
  x = [1,2,3,1,3,4]
  y = [1,2,3,2,3,4]
  plt.figure(figsize=(5,5), dpi=100)
  plt.title('Title', loc='left', pad=20, fontsize=20) #pad bu padding, loc bu 
  plt.text(3,1.5, "rangli text", fontsize=20, color='#1BBFE6', weight=1000, style='italic')
  plt.scatter(x, y, s=100)
  plt.show()
# figure()

def task1():
  x = [1,2,5,6,8]
  y = [1,2,3,7,5]
  plt.scatter(x,y,100,'red','.')
  for i in range(len(x)):
    plt.text(x[i], y[i], f'{(x[i], y[i])}')
  plt.show()

def task2():
  x1, y1, x2, y2 = [-1,1,3], [4,2,5], [1,1.5,0], [3,6,2]
  plt.scatter(x1,y1, label="Aylana") # label berish shart .legend ni ishlatish uchun
  plt.scatter(x2,y2, marker='s', label="To'rtburchak") # label berish shart .legend ni ishlatish uchun
  plt.legend(loc='lower right')
  plt.xlabel("X o'qi")
  plt.ylabel("Y o'qi")
  plt.show()

task2()