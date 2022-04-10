# List creation method time comparison

### Experiment is about measure time of creation lists of int elements depending on list size (number of elements append at the end of the list). There was used 3 different approach of creating new list:

- map function
- standard for loop with append at the end of the list
- list comprehension

**Setup:**
list size -from 0 to 10 000
time - summary time measuring creation list with different methods x times

According to how is implemented in Cpython which is default python implementation and the one we are using in this measurement, lists in CPython is dynamic array-like structure, which means that all elements is stored in one memory block consecutively, what differ CPython list from standard array implementation is that it can store different object types it is possible because of the fact that under the hood list indexes is contiguous references to other objects.

  In our measure we create new list by adding new element at the end of the list by using build-in append() list method, it is important because according to how list are when we add element in worst case  to the beggining we need to move all following elemetns in list by one position, also consider that when we create new list object an extra space is allocated so we are fine and don't need to reallocate for the next couple of appends, this result in amortized worst case time complexity of append to the end is O(1), constant, but some individual actions may be much longer (reallocate case).
  
  In our measure we create new lists from scratch size form 0 to 10 000, by appending int object from 0 to list-size -1, each operation should be O(1)*n, which result in O(n) in big-O notation, where n is the size of list (len list), the operation is repeated x times and the result is summary time of this x operations at each list-size, so it's make our measurement less prone to excetpions, however we can still notice locations where time is enormously big, it's particularly because over-allocate space in every list resize is a sequence of specific numbers proportional to list-size, which as mentioned earlier result in amortized linear time complexity of big-O notation.
