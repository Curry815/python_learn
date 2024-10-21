import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

# 读取数据文件
f = open("F:/可视化案例数据/地图数据/疫情.txt","r",encoding="UTF-8")
data = f.read()
# 关闭文件
f.close()
# 取到各省数据
# 将字符串json转换成python的字典
data_dict = json.loads(data)
# 从字典中取出省份数据
cities_data_list = data_dict["areaTree"][0]["children"][7]["children"]
# 定义存储绘图
data_list = []
# 组装每个省份和确诊人数为元组，并各个省的数据都封装入列表内
for cities_data in cities_data_list:
    cities_name = cities_data["name"]+"市"
    cities_confirm = cities_data["total"]["confirm"]
    data_list.append((cities_name, cities_confirm))
# 创建地图对象
map = Map()
# 添加数据
map.add("广东省疫情分布", data_list, "广东")
# 设置全局配置
map.set_global_opts(
    title_opts=TitleOpts(title="广东省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True, # 是否显示
        is_piecewise=True, # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100~999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000~4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000~9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000~99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000+", "color": "#990033S"},
        ]
    )
)
# 生成图表
map.render("广东省疫情地图.html")