from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts

# 读取文件
f = open("F:/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()

# 关闭文件
f.close()

# 删除第一条数据
data_lines.pop(0)

# 将数据转换为字典存储，格式为：
# {年份：[[国家, gdp], [国家, gdp], ...], 年份：[[国家, gdp], [国家, gdp], ...], ...}
# 先定义一个字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0]) # 年份
    country = line.split(",")[1] # 国家
    gdp = float(line.split(",")[2])  # gdp数据
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})

# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份前8个国家
    # year_data = data_dict[year][0:8]
    year_data = data_dict[year][8::-1]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0]) # x轴添加国家
        y_data.append(country_gdp[1] / 100000000) # y轴添加gdp
    # 构建柱状图对象
    bar = Bar()
    # 数据同步反转
    # x_data.reverse()
    # y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转x轴和y轴
    bar.reversal_axis()
    # 设置每一年的图表标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球GDP前8GDP")
    )

    timeline.add(bar, str(year))

# for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
# 在for中，将每一年的bar对象添加到时间线中

# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

# 绘图
timeline.render("1960-2019全球GDP前8国家.html")