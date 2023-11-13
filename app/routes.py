from flask import render_template, Response
from app import app


@app.route("/")
def index():
    return render_template("dashboard.html")


@app.route("/insight-1")
def get_data():
    import pandas as pd

    df = pd.read_csv("env/hadoop-hive-spark/notebooks/insight-1.csv")

    df.head()

    from highcharts_core.chart import Chart
    from highcharts_core.options import HighchartsOptions
    from highcharts_core.options.title import Title
    from highcharts_core.options.axes.x_axis import XAxis
    from highcharts_core.options.axes.y_axis import YAxis
    from highcharts_core.options.plot_options.scatter import ScatterOptions
    from highcharts_core.options.series.area import LineSeries
    from highcharts_core.options.axes.title import AxisTitle
    from highcharts_core.options.axes.accessibility import AxisAccessibility

    insight_1_a = LineSeries.from_pandas(
    df,
    series_type="line",
    property_map={"y": "renewables_consumption", "x": "year"},
    )

    insight_1_b = LineSeries.from_pandas(
        df,
        series_type="line",
        property_map={"y": "fossil_fuel_consumption", "x": "year"},
    )
    options = HighchartsOptions(
        title=Title(text="Trend of Energy Consumption over the years"),
        y_axis=YAxis(title=AxisTitle(text="Energy Consumption (Terawatt-hours)")),
        x_axis=XAxis(
            accessibility=AxisAccessibility(range_description="Year: 1990 to 2022")
        ),
    )
    insight_1 = Chart.from_options(options)
    insight_1.add_series(insight_1_a, insight_1_b)
    insight_1.container='chart'

    as_js_literal = insight_1.to_js_literal()

    return Response(as_js_literal, mimetype="application/javascript")
