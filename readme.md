# h3-python_example

## 安装

- pip

```
pip install h3
```

- conda

```
conda insatll h3-py
```

- 安装依赖

```
pip install -r requirements.txt
```

## quick start

```python
import h3
lat, lng = 37.769377, -122.388903
resolution = 9
h3.latlng_to_cell(lat, lng, resolution)
'89283082e73ffff'
```

## example

H3是一个层级化的六边形地理索引系统

此为学习过程中的笔记，且将原文件中的内容翻译为了中文，且原代码中有些代已无法运行，稍作修改后，仍有一部分代码不能运行。大佬如果有时间，快来看看bug~

> unified_data_layers.ipynb：此文件中有问题
>
> urban_analytics.ipynb：和其他代码重复度有点高，没做翻译笔记（实际是官网的示例代码）

此仓库来源于：https://github.com/uber/h3-py-notebooks.git

H3仓库：https://github.com/uber/h3-py.git

