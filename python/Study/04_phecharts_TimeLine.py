from pyecharts.charts import Timeline, Bar
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [300, 150, 20], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [400, 600, 100], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [100, 200, 600], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeLine = Timeline({
    "theme": ThemeType.LIGHT
})
timeLine.add(bar1, "点1")
timeLine.add(bar2, "点2")
timeLine.add(bar3, "点3")

timeLine.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
timeLine.render()
