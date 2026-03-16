import pandas as pd


def calculate_group_metrics(df):

    summary = df.groupby("group").agg(
        users=("user_id", "count"),
        conversions=("converted", "sum"),
        conversion_rate=("converted", "mean"),
        avg_revenue=("revenue", "mean")
    )

    return summary.reset_index()


def calculate_lift(control, treatment):

    return (treatment - control) / control