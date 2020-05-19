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

# Get the number of Clusters(k is num_clusters)
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
centroids = dict(zip(range(num_clusters),input_cluster_data[0:num_clusters]))
clusters = dict(zip(range(num_clusters),[[] for i in range(num_clusters)]))

# Tester Code to be deleted
print("centroids: ",centroids)
print("clusters: ",clusters)

# create and initialize a dict for mapping points in a cluster
# TODO modify to initialize a dict full of points
"""
point_assignments = {}
"""
point_assignments = {0: 1.2, 1: 3.4, 2: 6.7, 3: 4.9, 4: 5.0, 5: 5.0}

# Tester Code to be deleted
print("point_assignments: ",point_assignments)

# -create a variable to store old point assignments (from previous iteration)
old_point_assignments = {}

# Save current point assignment into old point assignment variable (create a new dict from current assignment variable) TODO
old_point_assignments = point_assignments

# Place each point in the closest cluster (you should make a function that does this)TODO
# point_assignments[j] = closest_index

#  Update the locations of centroids of the k clusters (make a function for this also)TODO

# Reinitialize the clusters variable to empty lists TODO
# clusters = dict(zip(range(k),[[] for i in range(k)]))

# Print the point assignments
# print(point_assignments[0:])
