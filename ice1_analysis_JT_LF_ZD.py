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
    df,           # the ANNdata object
    mt_exp_lvl_threshold):  # number between 0 and 1
    # gene_exp_threshold):   # number between 0 and 2000
    

    # filtering of the df
    return df[
        df["percent_mito"] <= mt_exp_lvl_threshold
        ].copy()

def filter_exp_cells(
    df,           # the ANNdata object
    # mt_exp_lvl_threshold,  # number between 0 and 1
    gene_exp_threshold):   # number between 0 and 2000
    

    # filtering of the df
    return df[
        df["n_genes"] >= gene_exp_threshold
        ].copy()


# Main
def main():
    # Load the AnnData object
    adata = ad.read_h5ad("./data/pbmc_sample.h5ad")

    percent_mito_threshold = 0.1 # filter to get those <= 0.1 % mito genes origin
    
    n_gene_threshold = 1500 # filter to get those >= 1500 genes expressed

    # 7b
    # Extract the DataFrame from the AnnData object
    df_original = adata.obs.copy()

    # Specify the column to sort by
    mt_column = df_original.columns[2]

    n_genes_column = df_original.columns[1]


    '''
    Running Recursive Versions of Sort Algorithms
    '''
    print("\nRecursive Sorts by:", mt_column)
    # Run Recursive Insert Sort Experiment
    print("Run insertionSort_recursive():")
    sorted_df_rec_insert = run_sort_experiment(df_original, mt_column, sort_func=insertionSort_recursive, descending=True)
    
    # Run Recursive Selection Sort Experiment
    print("Run selection_sort_recursive():")
    sorted_df_rec_selection = run_sort_experiment(df_original, mt_column, sort_func=selection_sort_recursive, descending=True)

    # Run Recursive Merge Sort Experiment
    print("Run merge_sort_recursive():")
    sorted_df_rec_merge = run_sort_experiment(df_original, mt_column, sort_func=merge_sort_rec, descending=True)


    # Run Recursive Quick Sort Experiment


    '''
    Running Iterative Versions of Sort Algorithms
    '''
    print("\nIterative Sorts by:", mt_column)
    # Run Iterative Insert Sort Experiment
    print("Run insertionSort_iter():")
    sorted_df_iter_insert = run_sort_experiment(df_original, mt_column, sort_func=insertionSort_iter, descending=True)

    # Run Iterative Selection Sort Experiment
    print("Run selection_sort_iter():")
    sorted_df_iter_selection = run_sort_experiment(df_original, mt_column, sort_func=selection_sort_iter, descending=True)

    # Run Iterative Merge Sort Experiment
    sorted_df_iter_merge = run_sort_experiment(df_original, mt_column, sort_func=merge_sort_iter, descending=True)

    
    # Run Iterative Quick Sort Experiment
    

    # 7c
    # using 7a function
    # calling the filtering function with the set values set: example
    percent_mito_threshold = 0.1 # filter to get those <= 0.1 % mito genes origin
    n_gene_threshold = 1500 # filter to get those >= 1500 genes expressed
    # df_mit_filtered = filter_mt_cells({your df}, 0.005585
    #                                 percent_mito_threshold, 
    #                                 ).obs.copy()

    # df_exp_filtered = filter_exp_cells({your df}, 
    #                                     # percent_mito_threshold, 
    #                                     ).obs.copy()
    
    # Validate if filtered correctly: dis has been validated
    # print(df_filtered.head())
    # print(f"percent_mito > {percent_mito_threshold} {(df_filtered["percent_mito"] > percent_mito_threshold).any()}")
    # print(f"n_genes < {n_gene_threshold} {(df_filtered["n_genes"] < n_gene_threshold).any()}")
    
    '''
    Results for Col3 mt expression
    '''
    print("\n----------------------------------------------------")
    print("\nResults for sorting Col3 mt expression:\n")

    #Filter slection sort results
    print("Selection Sort Recursive Results:")
    print("Recursive:")
    df_filtered_selection_rec = filter_mt_cells(sorted_df_rec_selection, percent_mito_threshold)
    print(df_filtered_selection_rec.tail())
    print(f"percent_mito > {percent_mito_threshold} {(df_filtered_selection_rec['percent_mito'] > percent_mito_threshold).any()}")

    print("Iterative:")
    df_filtered_selection_iter = filter_mt_cells(sorted_df_iter_selection, percent_mito_threshold)
    print(df_filtered_selection_iter.tail())
    print(f"percent_mito > {percent_mito_threshold} {(df_filtered_selection_iter['percent_mito'] > percent_mito_threshold).any()}")


    #Filter insert sort results
    print("Insert Sort Results:")
    print("Recursive:")
    df_filtered_insert_rec = filter_mt_cells(sorted_df_rec_insert, percent_mito_threshold)
    print(df_filtered_insert_rec.tail())
    print(f"percent_mito > {percent_mito_threshold} {(df_filtered_insert_rec['percent_mito'] > percent_mito_threshold).any()}")

    print("Iterative:")
    df_filtered_insert_iter = filter_mt_cells(sorted_df_iter_insert, percent_mito_threshold)
    print(df_filtered_insert_iter.tail())
    print(f"percent_mito > {percent_mito_threshold} {(df_filtered_insert_iter['percent_mito'] > percent_mito_threshold).any()}")

    
    #Filter Merge sort results
    print("Merge Sort Results:")
    print("Recursive:")
    df_filtered_merge_rec = filter_mt_cells(sorted_df_rec_merge, percent_mito_threshold)
    print(df_filtered_merge_rec.tail())
    print(f"percent_mito > {percent_mito_threshold} {(df_filtered_merge_rec['percent_mito'] > percent_mito_threshold).any()}")

    print("Iterative:")
    df_filtered_merge_iter = filter_mt_cells(sorted_df_iter_merge, percent_mito_threshold)
    print(df_filtered_merge_iter.tail())
    print(f"percent_mito > {percent_mito_threshold} {(df_filtered_merge_iter['percent_mito'] > percent_mito_threshold).any()}")



    
    #7d
    '''
    Running Recursive Versions of Sort Algorithms
    '''
    print("\n----------------------------------------------------")
    print("----------------------------------------------------")

    print("\nQUESTION 7d")
    print("\nSelection sort recursively by:", n_genes_column)

    #Run the filtered slection sort results to sort by n_genes column Recursively
    print("Run selection_sort_recursive():")
    sorted_df_filtered_selection_rec = run_sort_experiment(df_filtered_selection_rec, n_genes_column, sort_func=selection_sort_recursive, descending=False)
    #Run the filtered merge sort results to sort by n_genes column Recursively
    print("Run merge_sort_recursive():")
    sorted_df_filtered_merge_rec = run_sort_experiment(df_filtered_merge_rec, n_genes_column, sort_func=merge_sort_rec, descending=False)

    #Run the filtered Quick sort results to sort by n_genes column Recursively

    #Run the filtered insertion sort results to sort by n_genes column Recursively
    print("Run insertionSort_recursive():")
    sorted_df_filtered_insertion_rec = run_sort_experiment(df_filtered_selection_rec, n_genes_column, sort_func=insertionSort_recursive, descending=False)


    '''
    Running Iterative Versions of Sort Algorithms
    '''
    print("\nSelection sort iteratively by:", n_genes_column)
    #Run the filtered slection sort results to sort by n_genes column Iteratively
    print("Run selection_sort_iter():")
    sorted_df_filtered_selection_iter = run_sort_experiment(df_filtered_selection_iter, n_genes_column, sort_func=selection_sort_iter, descending=False)
    #Run the filtered merge sort results to sort by n_genes column Iteratively
    print("Run merge_sort_iter():")
    sorted_df_filtered_merge_iter = run_sort_experiment(df_filtered_merge_iter, n_genes_column, sort_func=merge_sort_iter, descending=False)
    
    #Run the filtered Quick sort results to sort by n_genes column Iteratively

    #Run the filtered insertion sort results to sort by n_genes column Recursively
    print("Run insertionSort_iter():")
    sorted_df_filtered_insertion_iter = run_sort_experiment(df_filtered_selection_iter, n_genes_column, sort_func=insertionSort_iter, descending=False)


    '''
    Results for Col2 number of genes expression
    '''
    print("\n----------------------------------------------------")
    print("\nResults for sorting Col2 number of genes expression:\n")

    #Filter selection sort results
    print("Selection Sort Recursive Results:")
    print("Recursive:")
    df_filtered_selection_rec = filter_exp_cells(sorted_df_filtered_selection_rec, n_gene_threshold)
    print(df_filtered_selection_rec.head())
    print(f"n_genes < {n_gene_threshold} {(df_filtered_selection_rec['n_genes'] < n_gene_threshold).any()}")

    print("Iterative:")
    df_filtered_selection_iter = filter_exp_cells(sorted_df_filtered_selection_iter, n_gene_threshold)
    print(df_filtered_selection_iter.head())
    print(f"n_genes < {n_gene_threshold} {(df_filtered_selection_iter['n_genes'] < n_gene_threshold).any()}")


    #Filter insert sort results
    print("Insert Sort Results:")
    print("Recursive:")
    df_filtered_insert_rec = filter_exp_cells(sorted_df_filtered_insertion_rec, n_gene_threshold)
    print(df_filtered_insert_rec.head())
    print(f"n_genes < {n_gene_threshold} {(df_filtered_insert_rec['n_genes'] < n_gene_threshold).any()}")

    print("Iterative:")
    df_filtered_insert_iter = filter_exp_cells(sorted_df_filtered_insertion_iter, n_gene_threshold)
    print(df_filtered_insert_iter.head())
    print(f"n_genes < {n_gene_threshold} {(df_filtered_insert_iter['n_genes'] < n_gene_threshold).any()}")

    #Filter merge sort results
    print("Merge Sort Results:")
    print("Recursive:")
    df_filtered_merge_rec = filter_exp_cells(sorted_df_filtered_merge_rec, n_gene_threshold)
    print(df_filtered_merge_rec.head())
    print(f"n_genes < {n_gene_threshold} {(df_filtered_merge_rec['n_genes'] < n_gene_threshold).any()}")

    print("Iterative:")
    df_filtered_merge_iter = filter_exp_cells(sorted_df_filtered_merge_iter, n_gene_threshold)
    print(df_filtered_merge_iter.head())
    print(f"n_genes < {n_gene_threshold} {(df_filtered_merge_iter['n_genes'] < n_gene_threshold).any()}")

    #Filter quick sort results
    print("Quick Sort Results:")
    print("Recursive:")


    print("Iterative:")



if __name__ == "__main__":
    main()
