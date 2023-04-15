'''
This is a wram up exercise to check total energy.

Author : Y. Gary Peng
Data   : March 13, 2023
Email  : garyphys0915@gapp.nthu.edu.tw
License: MIT
'''

def main():
  M = 1.5 
  G = 9.81
  
  lst_t = [0.004, 0.215, 0.417, 0.605, 0.813, 1.003, 1.209, 1.411, 1.602, 1.805]
  lst_v = [0.013, 0.679, 1.306, 1.920, 2.638, 3.236, 3.897, 4.516, 5.010, 5.803]
  lst_h = [2.004, 1.987, 1.988, 1.862, 1.684, 1.573, 1.327, 1.070, 0.768, 0.416]
  
  lst_tot = []
  for i in range(len(lst_t)):
    potential = M * G * lst_h[i]
    kenetic   = 0.5 * M * lst_v[i]**2 
    lst_tot.append(potential + kenetic)
    
  print('The total energy:\n', 
        lst_tot)
  print('The mean of the total energy:\n', 
        sum(lst_tot)/len(lst_tot))
  
if __name__ == '__main__':
  main()