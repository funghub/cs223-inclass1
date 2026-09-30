import anndata as ad

from sort_and_search_funs import selection_sort_iter, selection_sort_recursive
# from sort_and_search_funs import * # use * to import all functions instead of just those two?

from util_funs import timer_decorator


# Iterative Selection Sort Experiment
@timer_decorator
def run_selection_sort_iter(df_original, mt_column):
    # Fresh copy of original unsorted DataFrame
    df = df_original.copy()

    return selection_sort_iter(
        df,
        mt_column,
        descending=True
    )

# Recursive Selection Sort Experiment
@timer_decorator
def run_selection_sort_rec(df_original, mt_column):
    # Fresh copy of original unsorted DataFrame
    df = df_original.copy()

    return selection_sort_recursive(
        df,
        mt_column,
        descending=True
    )

# Main
def main():
    # Load the AnnData object
    adata = ad.read_h5ad("./data/pbmc_sample.h5ad")

    # Extract the DataFrame from the AnnData object
    df_original = adata.obs.copy()

    # Specify the column to sort by
    mt_column = df_original.columns[2]

    print("\nSorting by:", mt_column)

    # Run Iterative Selection Sort Experiment
    sorted_df_iter = run_selection_sort_iter(df_original, mt_column)

    # Run Recursive Selection Sort Experiment
    sorted_df_rec = run_selection_sort_rec(df_original, mt_column)


if __name__ == "__main__":
    main()
