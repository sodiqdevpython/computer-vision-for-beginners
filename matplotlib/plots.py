import matplotlib.pyplot as plt

def plot1():
  x = [0,1,2]
  y = [3,5,2]

  plt.plot(x,y,color='red')
  plt.show()

def plot2():
  x = [0,1,2,3]
  y = [3,5,2,7]
  plt.plot(x,y,c='red', label='qizil chiziq', 
          alpha=0.7,linestyle='dashdot',
          linewidth=3, marker='s',
          mec='blue', mew=3, 
          mfc='yellow', ms=15)
  plt.grid(axis='y', alpha=0.7, color='pink', lw=2, ls=':')
  #1)alpha bu rangni to'yiqlilik darajasi [0:1] bo'ladi
  #2)linestyle bu chiziqning usuli [solid, dashed, dashdot, dotted]
  #3)linewidth yoki lw deb belgilanadi va u chiziqning qalinligi
  #4)marker bu x va y kesishgan nuqtaning shakli
  #5)markeredgecolor yoki mec markerning borderining rangi
  #6)markeredgewidth yoki mew bu markerning qalinligi
  #7)markerfacecolor yoki mfc bu markerning o'rtasini rangi
  #8)markersize yoki ms bu markerning kattaligi
  #9).grid bu katak qo'shib beradi
  #10)axis=y bu faqat y o'qi uchun grid qo'shish
  #11)alpha=0.7 bu grid ning rangini to'yiqlilik darajasi [0:1] 
  #12)color bu rangi, lw bu linewidth, ls bu linestyle degani
  plt.legend(loc='upper left')
  plt.show()

plot2()