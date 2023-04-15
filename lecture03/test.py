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

def bi(a, b, pos, t, err, theta=45):
  i = 0
  m = 0 # default value
  while 0.5*(b - a) > err:
    m = 0.5*(a + b)
    print(0.5*(b - a))
    i+=1
    pos      = cla(pos, m, theta, t)
    pos_temp = cla(pos, a, theta, t)
    if pos_temp.all()*pos.all() < 0:
      b = m
    else:
      a = m
    
    if i > 10:
      raise ValueError('Too long!')
  print('v0 =', m)
  return m

def main(pig, x0, y0, theta, a, b):
  t    = 0
  dt   = 0.1
  pos  = np.array([x0, y0])
  err = 1
  tor  = 5 # pig radius + bird radius
  
  while True:
    v0 = bi(a, b, pos, t, err, theta=45)
    if d(pig, pos, v0, theta, t) < tor:
      print(d(pig, pos, v0, theta, t))
      if t > 10:
        print('Game over! Take too much time.')
        break
      else:
        print(f'Consume {t} [time unit]')
        print('Hit the PIG!')
        break
    elif pos[1] < pig[1] or pos[0] > pig[0]:
      print('Out of the filed!')
      break
    t += dt
  
if __name__ == '__main__':
  
  # print('''quit the game, please type: quit() \nSTART --> input initial interval [a, b]:''')
  # try:
  #   a = float(input('a (need a float): \n'))
  #   b = float(input('b (need a float): \n'))
  # except:
  #   print('Need to input float!!')
  # print('Valid interval input.')
  
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
  #   theta = float(theta)
  #   if theta < 90 and theta > 0:
  #     break
  #   else:
  #     print('Angel needs to be between 0 and 90!')
  # print('Input correct!')
  
  a, b = 0.1, 10
  pig = np.array([100, 0])
  x0, y0 = 0, 0
  main(pig, x0, y0, 45, 0.1, 10)