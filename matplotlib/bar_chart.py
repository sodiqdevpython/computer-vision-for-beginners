from matplotlib import pyplot as plt

def bar_chart():
  x = ['A','B']
  height = [7,5]
  width = [0.5, 0.7]
  colors = ['red', 'green']
  plt.bar(x, height, width, color=colors, bottom=[0,1])
  plt.show()


def practise1():
  data = {
    'Python': 13.33,
    'C': 11.41,
    'C++': 10.63,
    'Java': 10.33,
    'C#': 7.04,
    'JavaScript': 3.29,
    'Visual Basic': 2.64,
    'SQL': 1.53,
    'Assembley': 1.34,
    'PHP': 1.27
  }

  x = list(data.keys())
  height = list(data.values())
  plt.figure(figsize=(12,5), dpi=100)
  plt.barh(x, height)
  plt.title('TIOBE Index for August 2023', fontsize=20)
  plt.xlabel('Programming Languages', fontsize=16)
  plt.ylabel('Ratings', fontsize=16)
  plt.show()

practise1()