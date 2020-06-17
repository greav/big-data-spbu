# Big Data SPbU

## Task 1
Results are demonstrated [here](https://github.com/greav/big-data-spbu/blob/master/task1/task1.ipynb)

## Task 2
In this task, 32, 48 and 64 bit numbers were tested, because 128 bit numbers take up too much time
using a naive prime factorization algorithm.

|method    |n_numbers|n_bits|result|elapsed_time (milliseconds) |
|----------|---------|------|------|------------|
|sequential|2000     |32    |32686 |2577        |
|primitives|2000     |32    |32686 |962         |
|rx        |2000     |32    |32686 |1103        |
|sequential|2000     |48    |36381 |342402      |
|primitives|2000     |48    |36381 |190726      |
|rx        |2000     |48    |36381 |187827      |
|sequential|2000     |64    |9839  |12156237    |
|primitives|2000     |64    |9839  |6783499     |
|rx        |2000     |64    |9839  |6867575     |

## Task 3
Results are demonstrated [here](https://github.com/greav/big-data-spbu/blob/master/task3/task3.ipynb)
