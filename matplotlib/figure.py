import matplotlib.pyplot as plt

def figure():
  x = [1,2,5,6,7,8]
  y = [1,2,3,7,2,5]
  markers = ['.','*','s','v','3','1']
  plt.figure(figsize=(5,5),dpi=100, facecolor='red', edgecolor='green')
  for i in range(len(x)):
    plt.scatter(x[i], y[i], s=100, marker=markers[i])
  plt.savefig('1.jpg') # yoki .png (bu yerda saqlaydi rasmni)plt.savefig('1.jpg') # yoki .png (bu yerda saqlaydi rasmni)
  plt.show()
figure()