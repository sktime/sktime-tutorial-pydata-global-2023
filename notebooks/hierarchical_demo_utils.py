import numpy as np
from sktime.utils._testing.hierarchical import _make_hierarchical


def load_product_hierarchy():
    # Get daily historic sales and rename columns and indexes according to hierarchy above
    n_years = 5
    y = (
        _make_hierarchical(
            hierarchy_levels=(2, 4),
            min_timepoints=365 * n_years,
            max_timepoints=365 * n_years,
            random_state=0,
        )
        .drop(
            index=[
                ("h0_0", "h1_2"),
                ("h0_0", "h1_3"),
                ("h0_1", "h1_0"),
                ("h0_1", "h1_1"),
            ]
        )
        .rename(
            index={
                "h0_0": "Food preparation",
                "h0_1": "Food preservation",
                "h1_0": "Hobs",
                "h1_1": "Ovens",
                "h1_2": "Fridges",
                "h1_3": "Freezers",
            }
        )
        .reset_index()
        .rename(
            columns={
                "h0": "Product line",
                "h1": "Product group",
                "time": "Date",
                "c0": "Sales",
            }
        )
    )

    # Set date as monthly as sales as int and aggregate date
    y["Date"] = y["Date"].dt.to_period("M")
    y = y.groupby(by=["Product line", "Product group", "Date"]).sum()

    # Add noise to have different time series
    noise = np.random.RandomState(seed=0).normal(1, 0.3, np.shape(y))
    y = (y * noise).round(0)

    return y
