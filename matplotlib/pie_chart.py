import matplotlib.pyplot as plt

def pie_chart():
  x = [10,20,30]
  labels = ['A','B','C']
  explode = [0.1, 0, 0]
  """
  bu yerda explode bo'layabdi
  ya'ni bir biridan ajratayabdi
  """
  plt.pie(x, labels=labels, explode=explode)
  plt.show()

pie_chart()