# coding: utf-8 # <- This is an encoding declaration

import anndata as ad


from sort_and_search_funs import * # use * to import all functions instead of just those two?

from util_funs import timer_decorator


# Run Sort Experiment
@timer_decorator
def run_sort_experiment(df_original, sort_column, sort_func, descending):
    # Fresh copy of original unsorted DataFrame
    df = df_original.copy()

    return sort_func(
        df,
        sort_column,
        descending=descending
    )

# 7a
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
def filter_mt_cells(
    anndata_obj,           # the ANNdata object
    mt_exp_lvl_threshold):  # number between 0 and 1
    # gene_exp_threshold):   # number between 0 and 2000
    

    # filtering of the anndata_obj
    anndata_obj_filtered = anndata_obj[
        (anndata_obj.obs["percent_mito"] <=  mt_exp_lvl_threshold), :].copy()

    return anndata_obj_filtered

def filter_exp_cells(
    anndata_obj,           # the ANNdata object
    # mt_exp_lvl_threshold,  # number between 0 and 1
    gene_exp_threshold):   # number between 0 and 2000
    

    # filtering of the anndata_obj
    anndata_obj_filtered = anndata_obj[
        (anndata_obj.obs["n_genes"] >=  gene_exp_threshold), :].copy()

    return anndata_obj_filtered


# Main
def main():
    # Load the AnnData object
    adata = ad.read_h5ad("./data/pbmc_sample.h5ad")


    # 7b
    # Extract the DataFrame from the AnnData object
    df_original = adata.obs.copy()

    # Specify the column to sort by
    mt_column = df_original.columns[2]

    print("\nSorting by:", mt_column)

    '''
    Running Recursive Versions of Sort Algorithms
    '''
    # Run Recursive Insert Sort Experiment
    # sorted_df_rec_insert = run_sort_experiment(df_original, mt_column, sort_func=insertionSort_recursive)
    
    # Run Recursive Selection Sort Experiment  
    sorted_df_rec_selection = run_sort_experiment(df_original, mt_column, sort_func=selection_sort_recursive, descending=True)

    # Run Recursive Merge Sort Experiment

    # Run Recursive Quick Sort Experiment


    '''
    Running Iterative Versions of Sort Algorithms
    '''
    # Run Iterative Insert Sort Experiment
    # sorted_df_iter_insert = run_sort_experiment(df_original, mt_column, sort_func=insertionSort_iter)

    # Run Iterative Selection Sort Experiment
    sorted_df_iter_selection = run_sort_experiment(df_original, mt_column, sort_func=selection_sort_iter, descending=True)

    # Run Iterative Merge Sort Experiment
    
    # Run Iterative Quick Sort Experiment
    
    






    # 7c
    # using 7a function
    # calling the filtering function with the set values set: example
    percent_mito_threshold = 0.1 # filter to get those <= 0.1 % mito genes origin
    n_gene_threshold = 1500 # filter to get those >= 1500 genes expressed
    # df_mit_filtered = filter_mt_cells({your df}, 
    #                                 percent_mito_threshold, 
    #                                 ).obs.copy()

    # df_exp_filtered = filter_exp_cells({your df}, 
    #                                     # percent_mito_threshold, 
    #                                     ).obs.copy()
    
    # Validate if filtered correctly: dis has been validated
    # print(df_filtered.head())
    # print(f"percent_mito > {percent_mito_threshold} {(df_filtered["percent_mito"] > percent_mito_threshold).any()}")
    # print(f"n_genes < {n_gene_threshold} {(df_filtered["n_genes"] < n_gene_threshold).any()}")
    

if __name__ == "__main__":
    main()
