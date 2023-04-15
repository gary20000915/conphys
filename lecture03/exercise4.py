'''
This is the code for exercise 4 in lecture 03.

Author: Gary P.
E-mail: garyphys0915@gapp.nthu.edu.tw
'''

import matplotlib.pyplot as plt
import numpy as np


def cla(pos, v0, theta, t):
  g = -9.81 # m/s^2
  x = pos[0] + v0*np.cos(180*theta/np.pi)*t
  y = pos[1] + v0*np.sin(180*theta/np.pi)*t + 0.5*g*np.square(t)
  return np.array([x, y])

def d(pig, pos, v0, theta, t):
  return np.sqrt(np.sum(np.square(cla(pos, v0, theta, t) - np.array([pig]))))

def main(pig, x0, y0, v0, theta):
  t    = 0
  dt   = 1.e-2
  px = np.array([x0])
  py = np.array([y0])
  pos  = np.array([x0, y0])
  tor  = 5 # pig radius + bird radius
  
  while True:
    if d(pig, pos, v0, theta, t) < tor or t > 10:
      if t > 1.e2:
        print('Game over! Take too much time.')
        break
      else:
        print(pig, pos, v0, theta)
        print(f'Consume {t} [time unit]')
        print('Hit the PIG!')
        break
    elif pos[1] < pig[1] or pos[0] > pig[0]:
      print('Out of the filed!')
      break
      
    pos = cla(pos, v0, theta, t)
    px = np.append(px, pos[0])
    py = np.append(py, pos[1])
    t += dt
  plt.plot(px, py)
  plt.show()
  
if __name__ == '__main__':
  
  # print('quit the game, please type: quit()')
  
  # while True:
  #   v0 = input('input initial velocity (m/s): \n')
  #   if v0 == 'quit()':
  #     raise ValueError('quit')
  #   v0 = float(v0)
  #   if v0 < 1.e2:
  #     break
  #   else:
  #     print('Velocity is too large!')
    
  # while True:
  #   theta = input('input initial angel (degree): \n')
  #   if theta == 'quit()':
  #     raise ValueError('quit')
  #   theta =float(theta)
  #   if theta < 90 and theta > 0:
  #     break
  #   else:
  #     print('Angel needs to be between 0 and 90!')

  # print('Input correct!')
  v0, theta = 3.8, 60
  pig = np.array([100, 0])
  x0, y0 = 0, 0
  main(pig, x0, y0, v0, theta)