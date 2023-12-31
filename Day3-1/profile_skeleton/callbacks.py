import plotly.express as px
from dash.dependencies import Input, Output
from plotly import graph_objects as go

from utils import MBTI, random_avatar


def get_callbacks(app):
    @app.callback(
        Output("avatar","src"),
        Input("avatar-button","n-clicks",)
    )
    def update_avatar(clicks) :
        return random_avatar()
    
    @app.callback(
        Output("mbti", "figure"),
        Input("mbti-input", "value")
    )
    def update_pie_chart(mbti):
        color = px.colors.diverging.RdBu
        if mbti is not None:
            color = [
                "#FF1010" if mbti == m else "#323130"
                for m in MBTI
            ]
        pie_chart = go.figure(
            go.pie(
                value = [1] * 16,
                labels = MBTI,
                textinfo = "labels",
                hoverinfo = "labels",
                hole = 0.6,
                textfont={"size":20},
                markers = dict(colors = color) 
            )
        )

        pie_chart.update_layout(
            margin = dict(l = 0, r = 0, t = 0, b = 0),
            showlegend = False,
            paper_bgcolor="#323130",
        )
        return pie_chart
    
    @app.callback(
        Output("mbti-input", "value"),
        Input("mbti","clickData")
    )
    def update_mbti_input_from_pie_chart(mbti):
        if mbti is None:
            return None
        return mbti["points"][0]["label"]
    
    @app.callback(
        Output("name", "children"),
        Input("name-input")
    )
    def update_name(name):
        if name is None:
            return "이름"
        return f"이름 {name}"
    
    @app.callback(
        Output("age", "children"),
        Input("age-input")
    )
    def update_name(age):
        if age is None:
            return "이름"
        return f"나이 {age}"