import anndata as ad

def main():
    # Load the AnnData object
    adata = ad.read_h5ad("./data/pbmc_sample.h5ad")

    # # Extract the DataFrame from the AnnData object
    df_original = adata.obs.copy()

    # look at what datalooks like
    print(df_original.head()) # ANNdata converted to df
    print(adata) # look at ANNdata itself

    
    def filter_mt_cells(
        anndata_obj,           # the ANNdata object
        mt_exp_lvl_threshold,  # number between 0 and 1
        gene_exp_threshold):   # number between 0 and 2000
        '''
        Requirement for 7a.
        "cells that exhibit a high level of mitochondrial gene expression are 
        likely dead or dying cells, and the cell needs to be excluded from 
        the analysis"
    
        mt_exp_lvl_threshold: represents the percentage above which the 
        corresponding cell entry is to be eliminated from further consideration
        mitochontroal genes col3?
    
        gene_exp_threshold: represents the gene expression level below which the 
        corresponding cell entry is to be eliminated from further consideration
        number of genes expresed in cells col2?
        '''

        # filtering of the anndata_obj
        anndata_obj_filtered = anndata_obj[
            (anndata_obj.obs["percent_mito"] <=  mt_exp_lvl_threshold) & 
            (anndata_obj.obs["n_genes"] >=  gene_exp_threshold), :].copy()

        return anndata_obj_filtered
    
    # calling the filtering function with the set values set: example
    # set the thresholds you want to use for filtering (see summary stat line)
    percent_mito_threshold = 0.03 # filter to get those <= 0.03 % mito genes origin (outliers)
    n_gene_threshold = 1050 # filter to get those >= 1050 genes expressed
    df_filtered = filter_mt_cells(adata, 
                                  percent_mito_threshold, 
                                  n_gene_threshold
                                  ).obs.copy()
    # Check summary stats for both columns to know what thresholds to set
    # print(adata.obs[["percent_mito", "n_genes"]].describe())
        # choose percent_mito a little just below max to rid outliers
        # choose n_genes to filter out 25% below threshold
    
    # Validate if filtered correctly: uncoment to validate if needed; dis has been validated
    # print(df_filtered.head())
    # print(f"percent_mito > {percent_mito_threshold} {(df_filtered["percent_mito"] > percent_mito_threshold).any()}")
    # print(f"n_genes < {n_gene_threshold} {(df_filtered["n_genes"] < n_gene_threshold).any()}")

    # Check summary stats for both columns to know what threshold to set
    print(adata.obs[["percent_mito", "n_genes"]].describe())

    # # Specify the column to sort by
    # mt_column = df_original.columns[2]

    # print("\nSorting by:", mt_column)

    # # Run Iterative Selection Sort Experiment
    # sorted_df_iter = run_selection_sort_iter(df_original, mt_column)

    # # Run Recursive Selection Sort Experiment
    # sorted_df_rec = run_selection_sort_rec(df_original, mt_column)


if __name__ == "__main__":
    main()
