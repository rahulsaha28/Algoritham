# [Recursive Algorithm](https://www.youtube.com/watch?v=Mv9NEXX1VHc)



A algorithm is called recursive if it solves a problem by
reduce it to an `instance of the same problem` with a smaller input.


>> Recursion : Recursion is the process of repeating items in a self-similar way.

So taking a problem and reduce it a smaller version of that same problem.

So a function is call itself . But how time it's  called ?

The `condition` which stop the function call is called `base condition`.

#### State Variable : 
The variable which update for each iteration is called state variable.


  

### Example :

`GCD----> gretest common divider`

```
gcd(14, 20) -----------> 20 = 14(1) + 6
                             gcd(14,6)
gcd(14, 6)  ------------> 14 = 6(2) + 2
                            gcd(6,2)
gcd(6,2)   ------------> 6 = 2(3) + 0

                        gcd(2,0)
gcd(2,0)   -----------> 2

```

Now consider we have a function name fact(n) which work is
to multiply `n` and `fact(n-1)`

So we write `fact(n) = n * fact(n-1)`

Now if we find factorial that is

`5! = 5 * 4 * 3 * 2 * 1`

we use fact(n) function where ` fact(1) = 1`

```
fact(5) = 5 * fact(4)
                fact(4) = 4 * fact(3)
                               fact(3) = 3 * fact(2)
                                              fact(2) = 2 * fact(1)
                                                            fact(1) = 1
``` 
where base = fact(1) = 1

![](https://www.red-gate.com/simple-talk/wp-content/uploads/imported/901-DA3.JPG)


-----------------------------------
```
a*b = a+a+a+a.....+a
    = a+ a*(b-1)
    
So when b = 1,  a*b = a this is the base condition.



```
-----------------------------------

![](https://prasanthmadhavan.files.wordpress.com/2010/09/simplefact.png)


Resource
1. [MIT Lec](https://www.youtube.com/watch?v=WPSeyjX1-4s)
 
