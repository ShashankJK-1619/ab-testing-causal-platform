import pandas as pd
from metrics import calculate_group_metrics, calculate_lift
from stats_tests import conversion_test, revenue_test


def main():

    df = pd.read_csv("data/synthetic_experiment.csv")

    metrics = calculate_group_metrics(df)

    print(metrics)

    control = metrics[metrics.group == "control"].iloc[0]
    treatment = metrics[metrics.group == "treatment"].iloc[0]

    lift = calculate_lift(control.conversion_rate, treatment.conversion_rate)

    print("Conversion lift:", lift)

    z, p = conversion_test(df)

    print("Conversion p-value:", p)

    t, p2 = revenue_test(df)

    print("Revenue p-value:", p2)


if __name__ == "__main__":
    main()