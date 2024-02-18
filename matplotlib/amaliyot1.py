import matplotlib.pyplot as plt

def parabola():
  y = []
  for i in range(-40,41):
    y.append(i**2)
  
  plt.plot(y, linestyle='--', lw=3)
  #tepada x qo'shilmadi endi -40 dan emas 0 dan boshlaydi chizishni
  plt.text(35,600, "y = x ^ 2", size=20, style='italic')
  plt.title('Parabola')
  plt.xlabel('X'), plt.ylabel('Y')
  plt.show()

parabola()