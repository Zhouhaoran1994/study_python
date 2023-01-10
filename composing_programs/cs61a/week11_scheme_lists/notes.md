# Even Subsets (偶数和子集)
计算列表中的所有元素组合的和，返回偶数结果

提示需要满足以下三点：
1. all the even subsets of the rest  of s
2. the first element of s followed by an (even/odd) subset of the rest
3. just the first element of s if it is even

~~~
> (even-subsets ' (3 4 5 7))
((5 7) (4 5 7) (4) (3 7) (3 5) (3 4 7) (3 4 5))
~~~

## Even Subsets Using Filter

用filter改写上述需求

~~~

~~~