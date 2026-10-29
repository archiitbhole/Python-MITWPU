import numpy as np
import pandas as pd

# Sample dataset (student names, marks, cities)
data = {
    "Name": ["Aarav", "Diya", "Rohan", "Meera", "Rohan", "Kabir", "Ananya", "Sanya"],
    "Marks": [78, np.nan, 65, 88, 65, np.nan, 92, 54],
    "City": ["Pune", "Mumbai", "Pune", "Nagpur", "Pune", "Delhi", "Pune", None],
}
df = pd.DataFrame(data)

print("=== Original DataFrame ===")
print(df)

print("\n=== head() ===")
print(df.head(3))

print("\n=== info() ===")
df.info()

print("\n=== describe() ===")
print(df.describe())

print("\n=== Missing values per column ===")
print(df.isnull().sum())

# Handling missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())  # mean imputation
df["City"] = df["City"].fillna("Unknown")  # constant fill

print("\n=== After fillna() ===")
print(df)

# Removing duplicates
print("\n=== Duplicate rows ===")
print(df[df.duplicated()])

df = df.drop_duplicates().reset_index(drop=True)

print("\n=== After drop_duplicates() ===")
print(df)

# Filtering with loc[]
high_scorers_pune = df.loc[
    (df["Marks"] >= 60) & (df["City"] == "Pune"), ["Name", "Marks"]
]
print("\n=== loc[]: Pune students with Marks >= 60 ===")
print(high_scorers_pune)


#OUTPUT: 
'''
=== Original DataFrame ===
     Name  Marks     City
0   Aarav   78.0     Pune
1    Diya    NaN   Mumbai
2   Rohan   65.0     Pune
3   Meera   88.0   Nagpur
4   Rohan   65.0     Pune
5   Kabir    NaN    Delhi
6  Ananya   92.0     Pune
7   Sanya   54.0      NaN

=== head() ===
    Name  Marks    City
0  Aarav   78.0    Pune
1   Diya    NaN  Mumbai
2  Rohan   65.0    Pune

=== info() ===
<class 'pandas.DataFrame'>
RangeIndex: 8 entries, 0 to 7
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Name    8 non-null      object 
 1   Marks   6 non-null      float64
 2   City    7 non-null      object 
dtypes: float64(1), object(2)
memory usage: 324.0 bytes

=== describe() ===
           Marks
count   6.000000
mean   73.666667
std    14.814407
min    54.000000
25%    65.000000
50%    71.500000
75%    85.500000
max    92.000000

=== Missing values per column ===
Name     0
Marks    2
City     1
dtype: int64

=== After fillna() ===
     Name      Marks     City
0   Aarav  78.000000     Pune
1    Diya  73.666667   Mumbai
2   Rohan  65.000000     Pune
3   Meera  88.000000   Nagpur
4   Rohan  65.000000     Pune
5   Kabir  73.666667    Delhi
6  Ananya  92.000000     Pune
7   Sanya  54.000000  Unknown

=== Duplicate rows ===
    Name  Marks  City
4  Rohan   65.0  Pune

=== After drop_duplicates() ===
     Name      Marks     City
0   Aarav  78.00000
'''