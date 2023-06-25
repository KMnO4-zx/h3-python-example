# API速度比较


我们在各种API中对一个简单的demo计算任务进行计时。


我们还比较了在其中一种较快的API（使用H3索引的`int`表示法）中完成大部分计算，然后将结果转换为更熟悉的Python `str`对象格式的选项。


```python
import h3
import h3.api.numpy_int

# 定义一个函数，对给定的 H3 库进行一些计算
def compute(h3_lib, N=100):
    # 将经度 0，纬度 0 转化为一个 H3 索引，分辨率为9
    h   = h3_lib.geo_to_h3(0, 0, 9)
    # 生成一个包含中心索引和其 N 邻居索引的集合
    out = h3_lib.k_ring(h, N)
    # 将索引集合压缩为最小可能的集合
    out = h3_lib.compact(out)
    
    # 返回压缩后的集合
    return out

# 定义一个函数，对给定的 H3 库进行一些计算，并将结果转化为字符串形式
def compute_and_convert(h3_lib, N=100):
    # 调用 compute 函数进行计算
    out = compute(h3_lib, N)
    # 将结果（一个 H3 索引集合）转化为字符串形式
    out = [h3.h3_to_string(h) for h in out]
    
    # 返回字符串形式的结果
    return out

```

# 使用每个API计算

**基准测试注意事项**：`%%timeit sleep()`在执行剩余单元格中要计时的代码的每次**运行**前执行`sleep`；这有助于稳定计时结果（至少在我的笔记本电脑上是这样）。


```python
import time

def sleep():    
    time.sleep(2)
```


```python
%%timeit sleep()

compute(h3.api.basic_str)
```

    41.4 ms ± 906 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)



```python
%%timeit sleep()

compute(h3.api.basic_int)
```

    26.5 ms ± 1.22 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)



```python
%%timeit sleep()

compute(h3.api.memview_int)
```

    5.54 ms ± 155 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)



```python
%%timeit sleep()

compute(h3.api.numpy_int)
```

    5.25 ms ± 175 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)


# 计算' int ' api并转换为' str '


```python
%%timeit sleep()

compute_and_convert(h3.api.basic_int)
```

    25.1 ms ± 280 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)



```python
%%timeit sleep()

compute_and_convert(h3.api.memview_int)
```

    5.66 ms ± 88.1 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)



```python
%%timeit sleep()

compute_and_convert(h3.api.numpy_int)
```

    5.56 ms ± 77.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

