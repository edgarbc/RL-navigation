import pandas as pd
import numpy as np

class NominalToBinary:

    def __init__(self, infrequent_threshold=1):
        self.infrequent_threshold = infrequent_threshold
        self.new_values_counts = dict()

    def fit(self, df):

        self.new_values_counts = dict()
        self.features = []

        for col in df.columns:
            if np.issubdtype(df[col], np.number):
                self.features.append((col, df[col].dtype))

            else:
                # remove values that are infrequent (i.e. too specific)
                valCount = df.groupby([col])[col].transform('count')
                df.loc[valCount <= self.infrequent_threshold, col] = 'infrequent_value'

                self.features.append((col, pd.api.types.CategoricalDtype(df[col].unique(), ordered=False)))

    def transform(self, df, return_new_vals=False):

        new_df = pd.DataFrame()
        new_vals = dict()

        for col_type_tuple in self.features:
            col_name = col_type_tuple[0]
            col_type = col_type_tuple[1]
            new_df[col_name] = df[col_name].astype(col_type)

            # make note of any new categories encountered in this df
            if isinstance(col_type, pd.core.dtypes.dtypes.CategoricalDtype):
                this_col_new_vals = list(df[col_name][df[col_name] != new_df[col_name]])
                if len(this_col_new_vals) > 0:

                    for new_val in this_col_new_vals:
                        if new_val in self.new_values_counts:
                            self.new_values_counts[new_val] += 1
                        else:
                            self.new_values_counts[new_val] = 1

                    new_vals[col_name] = []
                    for new_val in set(this_col_new_vals):
                        new_vals[col_name].append((new_val, self.new_values_counts[new_val]))

        if return_new_vals:
            return pd.get_dummies(new_df), new_vals
        else:
            return pd.get_dummies(new_df)

    def fit_transform(self, df):
        self.fit(df)
        return self.transform(df)