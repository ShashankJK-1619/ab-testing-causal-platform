import numpy as np
from scipy.stats import ttest_ind
from statsmodels.stats.proportion import proportions_ztest


def conversion_test(df):

    control = df[df["group"] == "control"]["converted"]
    treatment = df[df["group"] == "treatment"]["converted"]

    successes = [treatment.sum(), control.sum()]
    nobs = [len(treatment), len(control)]

    stat, p_value = proportions_ztest(successes, nobs)

    return stat, p_value


def revenue_test(df):

    control = df[df["group"] == "control"]["revenue"]
    treatment = df[df["group"] == "treatment"]["revenue"]

    stat, p_value = ttest_ind(treatment, control)

    return stat, p_value