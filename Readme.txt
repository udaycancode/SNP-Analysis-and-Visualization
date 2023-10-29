# README for Code: SNP Analysis and Visualization

## Run the datasetGenerator.py to generate the dataset named result.csv

## Overview
This code performs a statistical analysis of Single Nucleotide Polymorphism (SNP) data and visualizes the results. It calculates p-values for each SNP, identifies significantly associated SNPs, applies Bonferroni correction, and creates a pseudo-Manhattan plot to visualize the data.

## Code Components

### 1. Data Processing
The code processes SNP data stored in a dataset and calculates p-values using Fisher's exact test for each SNP. It checks if each SNP is significant based on a predefined threshold (5e-8) and appends the results to a Pandas DataFrame.

### 2. Bonferroni Correction
It performs Bonferroni correction to control the family-wise error rate. The Bonferroni-corrected threshold is calculated based on a desired alpha level (0.05) and the total number of tests (1000). SNPs are then labeled as Bonferroni-significant if their p-value is below this threshold.

### 3. Data Visualization
The code uses Matplotlib to create a pseudo-Manhattan plot. This plot displays -log10(p-values) for each SNP and highlights the original and Bonferroni-corrected significance thresholds.

## Usage
1. Ensure that you have the required Python libraries, including Pandas and Matplotlib, installed.
2. Replace 'dataset' with your SNP data.
3. Set 'desired_alpha' to your desired significance level (alpha).
4. Update 'total_tests' with the total number of SNP tests you are performing.
5. Run the code to perform the analysis and generate the pseudo-Manhattan plot.
6. The results are saved in a CSV file named 'results.csv'.

## File Outputs
- 'results.csv': Contains SNP names, p-values, and labels for original and Bonferroni significance.
- A pseudo-Manhattan plot is displayed to visually represent the p-values.

## Notes
- Ensure that your dataset is appropriately formatted and contains the necessary columns for the analysis.
- The Bonferroni correction is used to control for multiple testing, but other correction methods may be more appropriate depending on your study design.
- Adjust the alpha level and the number of total tests according to your specific analysis.

This code is a basic template for SNP analysis and visualization and can be further customized to meet specific research requirements.