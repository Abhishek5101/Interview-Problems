"""

 was   - [-4,-1,0,3]
    index   |   value   |   response    |
      0     |     -4    |       16      |
      1     |    -1     |       1       |
      2     |    0      |       0       |
      3     |     3     |       9       |
      
now  [16,1,0,9]
sorted--> [0, 1, 9, 16]
"""


def sorted_squares(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] ** 2
    arr.sort()
    return arr


print(sorted_squares([-4,-1,0,3]))