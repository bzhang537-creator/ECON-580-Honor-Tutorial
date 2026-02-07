import numpy as np
import pandas as pd

# Load labels
keys = pd.read_csv("keys_to_X.csv")
posts = pd.read_csv("gendered_posts.csv")
keys_merged = pd.merge(keys, posts, on=["title_id", "post_id"], how="left")

# Training sample
i_train = keys_merged["training"] == 1
y = keys_merged.loc[i_train, "female"].values

# Load word-count matrix
wc = np.load("X_word_count.npz", allow_pickle=True)
X = wc["X"]

X_train = X[i_train.values, :]

# OLS coefficient for each word: cov(X_j, y) / var(X_j)
ols_me = []
for j in range(X_train.shape[1]):
    xj = X_train[:, j]
    if xj.var() == 0:
        ols_me.append(0.0)
    else:
        ols_me.append(np.cov(xj, y, bias=True)[0,1] / xj.var())

ols_me = np.array(ols_me)

# Load vocabulary
vocab = pd.read_csv("vocab10K.csv")
vocab["ME_OLS"] = ols_me

# Build Table 1 (OLS)
tab1_ols = pd.concat([
    vocab.sort_values("ME_OLS", ascending=False)[["word","ME_OLS"]].head(10).reset_index(drop=True),
    vocab.sort_values("ME_OLS", ascending=True)[["word","ME_OLS"]].head(10).reset_index(drop=True)
], axis=1)

print(tab1_ols)
tab1_ols.to_csv("table1_OLS.csv", index=False)
