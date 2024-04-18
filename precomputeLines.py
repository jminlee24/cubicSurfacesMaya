import numpy as np
import itertools


def remove_dups(l):
  new_k = []
  for el in l:
    dup = False
    for e in new_k:
      if np.array_equal(e, el):
        print(e, el)
        dup = True
        break
    if dup == False:
      new_k.append(el)
  return new_k


def get24Lines():
  t = np.linspace(-10, 10, 100)
  lines = {}
  for _k in range(2, 20):
    for i in range(3):
      for j in [-1, 1]:
        for k in [-1, 1]:
          coord = [0, 0, 0]
          coord[i] = np.sqrt(_k - 2) * j
          coord[(i + 1) % 3] = 2 * k

          shift = np.array([1 * k, 1, 0])
          shift = np.roll(shift, i - 1)
          if _k in lines:
            lines[_k].append(np.array([coord, shift]))
            lines[_k] = remove_dups(lines[_k])
          else:
            lines[_k] = [np.array([coord, shift])]
  return lines


print(get24Lines()[2])
