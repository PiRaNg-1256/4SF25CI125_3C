# Milestone 1: Cars Dataset EDA

Exploratory data analysis on a cars dataset (100,000 rows, 437 columns) using numpy, pandas, matplotlib and seaborn.

## Files

| File | Description |
|------|-------------|
| `cars_dataset.csv` | The dataset (about 233 MB), stored with Git LFS |
| `eda_cars.py` | Script that cleans the data and shows two plots |
| `.gitattributes` | Tells Git to track `*.csv` files with LFS |

## Git LFS and the CSV

GitHub rejects any single file over 100 MB. `cars_dataset.csv` is about 233 MB, so it is stored with [Git LFS](https://git-lfs.com/) (Large File Storage). The repository itself holds only a small pointer file. The real CSV is kept on LFS storage and downloaded when you clone or pull.

To get the actual CSV after cloning:

1. Install Git LFS from https://git-lfs.com/.
2. Set it up once per machine:

```bash
git lfs install
```

3. Clone as usual. LFS fetches the CSV automatically:

```bash
git clone <repo-url>
```

If you cloned before installing LFS, `cars_dataset.csv` will be a text file of a few lines instead of the dataset. Fix it with:

```bash
git lfs pull
```

If you see `version https://git-lfs.github.com/spec/v1` inside the CSV, it is still the pointer file.

## Running the script

Requires Python 3 with numpy, pandas, matplotlib and seaborn:

```bash
pip install numpy pandas matplotlib seaborn
```

Run from the repo folder so the CSV is found:

```bash
python eda_cars.py
```

The script prints the dataset shape and a summary, cleans the data, and opens two plot windows (close the first to see the second):

1. Distribution of final sale price.
2. Final sale price by body type (top 8 types).

## Cleaning steps

- Drop duplicate rows.
- Keep only sold cars (`final_sale_price` greater than 0). Unsold cars have a price of 0.
- Drop columns that are more than 50% empty.
- Fill missing numbers with the column median and missing text with `"Unknown"`.
- Clip `final_sale_price` to its 1st to 99th percentile range.
- Add `discount_percent_msrp`, the discount from MSRP to the final sale price.

## Pushing to a new repository

Git LFS must be installed on the machine you push from. The LFS tracking rule is already in `.gitattributes`.

```bash
git remote set-url origin <new-repo-url>
git push -u origin main
```
