import os
import argparse
import numpy as np
import pandas as pd

N_CASE = 50
N_CONTROL = 100
N_SNPS = 1000

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='GWAS dataset generator.')
    parser.add_argument('--ID', type=int, required=True, help='your 10 digits student ID, e.g. 1001234567')
    args = parser.parse_args()
    ID = args.ID
    rng = np.random.default_rng(ID)
    dataset_dict = {'SNP': [], 'Case_Num_C_Allele': [], 'Case_Num_T_Allele': [], 'Control_Num_C_Allele': [], 'Control_Num_T_Allele': []}

    for snp in range(N_SNPS):
        prob_case, prob_control = rng.random(), rng.random()

# 1 means C-Allele and 0 means T-Allelee
        case = rng.choice([0, 1], size=N_CASE, replace=True, p=[1-prob_case, prob_case])
        control = rng.choice([0, 1], size=N_CONTROL, replace=True, p=[1-prob_control, prob_control])
        A = np.sum(case)
        B = np.sum(control)
        X = N_CASE - A
        Y = N_CONTROL - B
        if A == 0:
            A = 1
            X = X -1
        elif X == 0:
            X = 1
            A = A - 1
        if B == 0:
            B = 1
            Y = Y - 1
        elif Y == 0:
            Y = 1
            B = B -1
        dataset_dict['SNP'].append('snp' + str(snp))
        dataset_dict['Case_Num_C_Allele'].append(A)
        dataset_dict['Case_Num_T_Allele'].append(X)
        dataset_dict['Control_Num_C_Allele'].append(B)
        dataset_dict['Control_Num_T_Allele'].append(Y)
    
dataset = pd.DataFrame(dataset_dict)
dataset.to_csv(str(ID)+".csv", header=True, index=False)