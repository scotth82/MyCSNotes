# Pandas

- [Pandas Project Site](https://pandas.pydata.org/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
  
- Common Commands
  ```python
  #import Pandas package
  import pandas as pd

  #show Pandas version
  pd.__version__
  ```

- **Data Structures - Series**
  ```python
  #series is a one-dimensional labled array holding any data type in column
  #optional index definition, default start from index 0
  
  data = [999, "x", True, None]
  pd.Series(data)

    0     999
    1       x
    2    True
    3    None

  index = ['a','b','c','d']
  pd.Series(data, index=index)

    a     999
    b       x
    c    True
    d    None

  data = {'a':999, 'b':'x', 'c':True, 'd':None}
  pd.Series(data)
  
    a     999
    b       x
    c    True
    d    None

  ```
- ??
- 
