data = pd.read_csv('res_dpre.csv')

with open('/home/doc-bd-a1/eda-in-1.txt', 'a') as file:
    data.to_csv(file, header=True)
    file.write("\n")

    summary_stats = data.describe()
    summary_stats.to_csv(file, header=True)
    file.write("\n")

    skewness = data.skew()
    skewness.to_csv(file, header=True)
    file.write("\n")

    correlation_matrix = data.corr()
    correlation_matrix.to_csv(file, header=True)
    file.write("\n")