import numpy as np
import pandas as pd


def generate_experiment_data(n_users=10000):

    user_id = np.arange(1, n_users + 1)

    group = np.random.choice(["control", "treatment"], n_users)
    device = np.random.choice(["mobile", "desktop"], n_users)

    pre_spend = np.random.gamma(2, 20, n_users)

    base_prob = 0.10
    treatment_effect = np.where(group == "treatment", 0.02, 0)

    conversion_prob = base_prob + treatment_effect

    converted = np.random.binomial(1, conversion_prob)

    revenue = converted * np.random.gamma(2, 30, n_users)

    df = pd.DataFrame({
        "user_id": user_id,
        "group": group,
        "device": device,
        "pre_spend": pre_spend,
        "converted": converted,
        "revenue": revenue
    })

    return df


if __name__ == "__main__":

    df = generate_experiment_data()

    df.to_csv("data/synthetic_experiment.csv", index=False)

    print(df.head())