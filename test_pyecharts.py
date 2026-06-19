from pyecharts.charts import Line
from pyecharts import options as opts

chart = (
    Line()
    .add_xaxis(["Jan","Feb","Mar"])
    .add_yaxis("Gold",[3200,3300,3380])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Gold Trend"
        )
    )
)

chart.render("gold.html")