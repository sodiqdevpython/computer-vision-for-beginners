#! Scatter plot ga kirish
import matplotlib.pyplot as plt

def birinchi_eng_oddiy_korinishi():
  plt.scatter(3,4)
  plt.show()

#! List ko'rinishida ham berish mumkin albatta faqat x va y lar soni teng bo'lsin

def ikkinchi():
  x = [2,4,1]
  y = [1,2,4]

  plt.scatter(x,y, 150) # 150 bu nuqtaning kattaligi
  plt.show()

def uchinchi():
  x = [2,1,4]
  y = [1,5,2]
  size = [100,200,300]
  color = [(234/255, 30/255, 88/255), '#195BAD', '#8EE525'] #! Bu yerda 1-sini hammasini 255 ga bo'ldim chunki RGB
  plt.scatter(x,y, size, color, marker='<')
  plt.show()

def uyga_vazifa():
  x = [1,2,5,6,7,8]
  y = [1,2,3,7,2,5]
  markers = ['.','*','s','v','3','1']
  for i in range(len(x)):
    plt.scatter(x[i], y[i], s=(i+1)*100, marker=markers[i])
  plt.show()


birinchi_eng_oddiy_korinishi()
ikkinchi()
uchinchi()
uyga_vazifa()