# Data Cleaning Pipeline

A Python script demonstrating common real-world data cleaning steps on a messy product dataset: duplicates, inconsistent types, inconsistent text, and missing values.

## How it works
1. **Remove duplicates** — drops duplicate SKUs, keeping the first occurrence
2. **Fix data types** — converts a mixed string/number `price` column to proper numeric values, turning invalid entries into `NaN` instead of crashing
3. **Standardize text** — cleans inconsistent category casing (`"clothing"`, `"CLOTHING"`, `"Clothing"`) into a single consistent format
4. **Drop incomplete rows** — removes rows missing a product name, since there's no reasonable way to guess it
5. **Flag missing data** — instead of guessing missing prices, flags them with a `needs_price_review` column for manual follow-up

## How to run
```bash
python data_cleaner.py
```

## What I learned
- Using `.drop_duplicates(subset=..., keep='first')` to remove duplicate records based on a specific column
- Using `pd.to_numeric(..., errors='coerce')` to safely convert mixed-type data, turning bad values into `NaN` instead of raising an error
- Using `.str.strip().str.title()` to normalize inconsistent text formatting
- Using `.dropna(subset=...)` to remove rows missing critical fields
- Flagging uncertain data instead of silently guessing or deleting it — an important data integrity principle

## Dependencies
Requires pandas and NumPy:
```bash
pip install pandas numpy
```
