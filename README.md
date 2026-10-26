# Country Data Analysis

A small Python and pandas project exploring a country dataset through questions about population, democracy scores, regions, and missing political-leader values.

## What it does

- Finds the capital cities associated with the maximum and minimum population values.
- Ranks countries by democracy score and prints the top five.
- Counts countries by region and reports the number of regions.
- Lists countries in Eastern Europe and identifies missing political-leader values.
- Loads and inspects the bundled CSV data with pandas and NumPy.

## Project files

- `Data_capstone/Countries.csv` — input dataset.
- `Data_capstone/Data_capstone.py` — analysis script.

## Run locally

Install Python 3 and the dependencies:

```bash
python -m pip install numpy pandas
```

Run the script from the `Data_capstone` directory so the relative CSV path resolves:

```bash
cd Data_capstone
python Data_capstone.py
```

The script prints region counts, Eastern Europe results, and countries with missing leader data. Some calculated values, including the minimum-population capital, are assigned but not currently printed.

## Scope

This is a compact pandas practice project. It performs direct queries on the supplied data; it does not currently include a separate cleaning pipeline, charts, or written interpretation of findings.
