"""Small ML demonstration using pandas, NumPy and scikit-learn."""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def main():
    rng = np.random.default_rng(42)
    X = rng.normal(size=(200, 4))
    y = (X[:, 0] + 0.7 * X[:, 1] > 0).astype(int)

    frame = pd.DataFrame(X, columns=["feature_1", "feature_2", "feature_3", "feature_4"])
    X_train, X_test, y_train, y_test = train_test_split(
        frame, y, test_size=0.2, random_state=42, stratify=y
    )

    model = make_pipeline(StandardScaler(), LogisticRegression(random_state=42))
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(f"NumPy samples: {X.shape[0]}")
    print(f"pandas columns: {list(frame.columns)}")
    print(f"Test accuracy: {accuracy_score(y_test, predictions):.3f}")


if __name__ == "__main__":
    main()
