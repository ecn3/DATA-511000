# Christian Nelson | Kanar Ibrahim
# 5/18/2020
# DATA-51100-002, SUMMER 2020
# PROGRAMMING ASSIGNMENT #2 kMeans

# Print header info to screen
print("Christian Nelson | Kanar Ibrahim")
print("5/18/2020")
print("DATA-51100-002, SUMMER 2020")
print("PROGRAMMING ASSIGNMENT #2 kMeans")

# Get input file name
input_file = raw_input("Enter the name of the input file: ")


# Tester Code to be deleted
input_file = 'prog2-input-data.txt'

# Get output file name
output_file = raw_input("Enter the name of the output file: ")

# Get the number of Clusters
num_clusters = int(raw_input("Enter the number of Clusters: "))

# Tester Code to be deleted
print("input_file: ", input_file)
print("output_file: ", output_file)
print("num_clusters: ", num_clusters)

# Read file
input_cluster_data = [float(x.rstrip()) for x in open(input_file)]

# Tester Code to be deleted
print(input_cluster_data[0:])

# Initialize variables for  centroids, clusters, and point assignments
centroids = dict(zip(range(k),input_cluster_data[0:k])
#clusters = dict(zip(range(k),[[] for i in range(k)]))
