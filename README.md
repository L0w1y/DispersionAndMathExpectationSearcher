# Math Expectation and Dispersion searcher

## How it works?
> At the beginning, after starting the program - it will ask you to set the number of columns,
> regardless of the number of columns - there will always be two rows.
> An example is presented below


|  num  | 1 | 2 | 3 | 4 | 5 |
| ---- | - | - | - | - | - |
| 1 | -1 | 2 | 5 | 10 | 20 |
| 2 | 0,1 | 0,2 | 0,3 | 0,3 | 0,1 |

```
1 - 1st String
2 - 2nd String
```


> To find the mathematical expectation, we multiply the rows in the columns and summarize the results. An example is given below


| № | 1 | 2 | 3 | 4 | 5 |
|---|--------|---|---|---|---|
| 1 | -1 | 2 | 5 | 10 | 20 |
| o | * | * | * | * | * |
| 2 | 0,1 | 0,2 | 0,3 | 0,3 | 0,1 |
| r | -0,1 | 0,4 | 1,5 | 3 | 2 |

```
1 - 1st String
o - Operation
2 - 2nd String
r - Results
```


| sum | 6,8 |
| --- | ---- |

> To find the Dispercy, we count the square of the first row, and multiply by the second row in the same column. - we get the square of the first row. We sum up the obtained data and get the Dispercion. An example is given below

| № | 1 | 2 | 3 | 4 | 5 |
|-|-|-|-|-|-|
| 1^2 | -1^2 | 2^2 | 5^2 | 10^2 | 20^2 |
| o | * | * | * | * | * |
| 2 | 0,1 | 0,2 | 0,3 | 0,3 | 0,1 |
| r | 0,1 | 0,8 | 7,5 | 30 | 40 |

```
1^2 - Square of 1st String
o - Operation
2 - 2nd String
r - Results
```

| sum | 78,4 |
| - | - |

> After the operations performed, we subtract the calculated Square of the first row from the Mathematical expectation and get the result of the Dispercy. An example is provided below

| Name | Values |
|-|-|
| Squared 1st String | 78,4 |
| Operation | - |
| Mathematical Exp^2 | 6,8^2 |
| Result | 32,16 |

> Dispercy is ` 32,16 `
