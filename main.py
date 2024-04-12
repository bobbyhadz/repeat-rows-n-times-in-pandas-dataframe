# How to repeat Rows N times in a Pandas DataFrame

import pandas as pd

df = pd.DataFrame({
    'first_name': ['Alice', 'Bobby', 'Carl'],
    'salary': [175.1, 180.2, 190.3],
})

df2 = df.loc[df.index.repeat(2)]

print(df2)