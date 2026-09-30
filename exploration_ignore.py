import anndata as ad

def main():
    # Load the AnnData object
    adata = ad.read_h5ad("./data/pbmc_sample.h5ad")

    # # Extract the DataFrame from the AnnData object
    df_original = adata.obs.copy()

    print(df_original.head())

    # # Specify the column to sort by
    # mt_column = df_original.columns[2]

    # print("\nSorting by:", mt_column)

    # # Run Iterative Selection Sort Experiment
    # sorted_df_iter = run_selection_sort_iter(df_original, mt_column)

    # # Run Recursive Selection Sort Experiment
    # sorted_df_rec = run_selection_sort_rec(df_original, mt_column)


if __name__ == "__main__":
    main()
