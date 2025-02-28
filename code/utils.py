import h3  # H3地理网格系统库，用于处理六边形网格化地理数据
import geopandas  # 地理数据处理库，基于pandas扩展，支持空间数据操作
import geodatasets  # 提供示例地理数据集
import contextily as cx  # 底图工具，用于添加网络地图背景
import matplotlib.pyplot as plt  # 绘图库，用于数据可视化


def plot_df(df, column=None, ax=None):
    """基于GeoPandas DataFrame的几何列绘制地图
    :param df: GeoDataFrame，包含几何列的地理数据
    :param column: 可选，用于分类着色显示的列名
    :param ax: 可选，matplotlib的轴对象，用于在指定轴上绘图
    """
    df = df.copy()  # 创建副本避免修改原始数据
    df = df.to_crs(epsg=3857)  # 转换为Web Mercator投影（EPSG:3857），这是网络地图的标准投影

    # 如果未提供轴对象，则创建新图形
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 8))  # 创建8x8英寸的图形
    
    # 隐藏坐标轴刻度
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # 绘制地理数据
    df.plot(
        ax=ax,
        alpha=0.5,  # 设置透明度
        edgecolor='k',  # 边界颜色为黑色
        column=column,  # 指定分类列
        categorical=True,  # 按分类数据渲染
        legend=True,  # 显示图例
        legend_kwds={'loc': 'upper left'},  # 图例位置在左上角
    )
    # 添加底图（使用CartoDB的Positron风格）
    cx.add_basemap(ax, crs=df.crs, source=cx.providers.CartoDB.Positron)


def plot_shape(shape, ax=None):
    """绘制单个几何形状
    :param shape: 几何对象（如Polygon，需符合GeoJSON格式）
    :param ax: 可选，matplotlib的轴对象
    """
    # 将几何对象转换为GeoDataFrame（坐标系为WGS84, EPSG:4326）
    df = geopandas.GeoDataFrame({'geometry': [shape]}, crs='EPSG:4326')
    plot_df(df, ax=ax)


def plot_cells(cells, ax=None):
    """绘制H3网格单元
    :param cells: 包含H3单元格ID的列表（例如['891e2034b7fffff', ...]）
    :param ax: 可选，matplotlib的轴对象
    """
    # 将H3单元格ID集合转换为多边形几何对象
    shape = h3.cells_to_h3shape(cells)
    plot_shape(shape, ax=ax)


def plot_shape_and_cells(shape, res=9):
    """并排显示原始形状与对应H3网格化的效果
    :param shape: 原始几何形状（如城市边界）
    :param res: H3网格分辨率（0-15，数值越大网格越小）
    """
    # 创建1行2列的子图，共享坐标轴
    fig, axs = plt.subplots(1, 2, figsize=(10, 5), sharex=True, sharey=True)
    
    # 在左子图绘制原始形状
    plot_shape(shape, ax=axs[0])
    # 在右子图绘制对应分辨率的H3网格
    plot_cells(h3.h3shape_to_cells(shape, res), ax=axs[1])
    
    # 调整子图布局
    fig.tight_layout()