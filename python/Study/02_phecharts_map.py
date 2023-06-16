from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
data = [
    ("北京市", 100),
    ("上海市", 200),
    ("贵州省", 20),
    ("湖南省", 400),
    ("武汉省", 500)
]

map.add("测试地图", data, "china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 100, "label": "10-100人", "color": "#FF6666"},
            {"min": 101, "max": 500, "label": "101-500人", "color": "#990033"},
        ]
    )
)
map.render()
