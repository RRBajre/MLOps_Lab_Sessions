from sklearn.base import BaseEstimator, TransformerMixin


class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    # Extract fist letter of variable

    def __init__(self, variables):
        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        for var in self.variables:
            X[var] = X[var].apply(lambda x: x[0] if type(x) == str else x)
        return X
