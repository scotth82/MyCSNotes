#COMP 682 Algorithms
**ToDo:**
- [ ] Horner's Rule Solving Polynomials
- [ ] Reivew Log operation
- [ ] Review videos again
- [ ] Finish M1 Problem Set


##What Is An Algorithm?
- Arecipe for a computation
- A computer program that computes something
- An algorithm always halts!

## 2 Fundamentals in CS
- How to compute the desired answer
- How to write program that compute the answer
  
## How Do We Evaluate Algorithms?
- Determine worst-case and expected-case consumption of computational resource
- Running time and memory
- Performance function of an algorithm is Computational Complexity
- We often compare the large n behavior is called asymptotic complexity

## Horner's Rule
- dfd

## Searching Problem - find if v is in an ordered set
- Naive Search
  - Ignore ordering, go through array 1 at a time
  - O(n)
- Binary Search : Divide-and-Conquer
  - Use ordering, always start from the middle, search right side if v is larger, search left side if v is smaller, take smaller of the middle two numbers if even
  - O(log(n))
  - 20 binary searchs vs. 1mm naive searches in a 1mm array
  - Always use binary search, way more efficient

## Computing O(n)
- Loop bounds/trip counts of loop determine factors
- Nesting level multiples factors from each nesting level
- Most deeply nested loops control BigO complexity
  
## Algorithm Design Principles
- DNR (Do Not Repeat)
- Divide-and-conquer : often implemented using recursion
- Pay it forward
- Greedy (optimization)
- Dynamic Programming **