
import pandas as pd
import numpy as np
import time
import random

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy.stats as st
import seaborn.objects as so
import seaborn as sns

def run_RSA_tests_with_plot():
  data = pd.DataFrame(columns=["RngRun","Długość klucza","CToR","Czas wykonania (s)"])

  mults = [1,2,4,8,16,32]
  CRT_modes = [False, True]
  for i in range(2):
    for m in mults:
      test_public, test_private = get_RSA_key_pair(m)
      for c in CRT_modes:
        t_elapsed = test_RSA_text(test_public,test_private,c)
  
        new_row = {
          "RngRun": i,
          "Długość klucza": m*8*BLOCK_SIZE,
          "CToR": c,
          "Czas wykonania (s)": t_elapsed
        }
        data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)

  print(data)

  plot_sum = data.groupby(["Długość klucza","CToR"])["Czas wykonania (s)"].mean().reset_index()
  
  print(plot_sum)

  hue = plot_sum["CToR"].astype(str)
  ax = sns.lineplot(data=plot_sum, x='Długość klucza', y='Czas wykonania (s)', hue=hue, errorbar=None, marker='o')
  plt.legend(title="CToR?")
  sns.move_legend(ax, "upper left")

  ax.set(xlabel='Długość klucza RSA [bity]', ylabel='Czas wykonania [s]')
  plt.gcf().set_facecolor("#f5f2eb" )  # Kolor całego tła figury
  # Dodanie wartości na osi X jako liczby całkowite 
  xticks = range(0, plot_sum['Długość klucza'].max() + 1, 256)
  plt.xticks(xticks)

  plt.savefig('curve.svg')