# Christian Nelson | Kanar Ibrahim
# 5/18/2020
# DATA-51100-002, SUMMER 2020
# PROGRAMMING ASSIGNMENT #2 kMeans

# Format String
fmt = "Point {} in cluster {}\n"

# Print header info to screen
print("Christian Nelson | Kanar Ibrahim")
print("5/18/2020")
print("DATA-51100-002, SUMMER 2020")
print("PROGRAMMING ASSIGNMENT #2 kMeans")

# Get input file name not using raw_input as that is for python 2 and causes errors
input_file = input("Enter the name of the input file, ex 'prog2-input-data.txt': ")

# Get output file name
output_file = input("Enter the name of the output file: ")

# Get the number of Clusters(k is num_clusters)
num_clusters = int(input("Enter the number of Clusters: "))

# Read file
input_cluster_data = [float(x.rstrip()) for x in open(input_file)]

# Initialize variables for  centroids, clusters, and point assignments
centroids = dict(zip(range(num_clusters),input_cluster_data[0:num_clusters]))
clusters = dict(zip(range(num_clusters),[[] for i in range(num_clusters)]))

# create and initialize a dict for mapping points in a cluster
point_assignments = {0: 1.2, 1: 3.6, 2: 5.0, 3: 5.0, 4: 7.6, 5: 10.0, 6: 3.7}
# print list
print_point_assignments = {}

# -create a variable to store old point assignments (from previous iteration)
old_point_assignments = {}

# Save current point assignment into old point assignment variable (create a new dict from current assignment variable)
old_point_assignments = point_assignments

# Function for placing each point in the closest cluster
def assign_to_clusters(input_cluster_data, clusters, centroids, point_assignments):
    # Initialize centroid_comparator
    centroid_comparator = 100
    # Iterate through each point in the point_assignments dict
    for idx, x in enumerate(point_assignments):
        # compare it against all the centroids
        for idx_n, y in enumerate(centroids):
            # Get the difference in the centroid and the point
            new_centroid_comparator = abs(centroids[idx_n] - point_assignments[idx])
            if centroid_comparator > new_centroid_comparator:
                centroid_comparator = new_centroid_comparator
                closest_index = y
                # Assign the cluster location to our print list
                print_point_assignments[x] = idx_n
        # Add point to the list of points for that cluster
        clusters[closest_index].append(point_assignments[idx])
        # Reset centroid comparator
        centroid_comparator = 100
            
#  Update the locations of centroids of the k clusters (make a function for this also)
def update_centroids(input_cluster_data, clusters, centroids):
    # Initialize centroid
    centroid = 0
    for x in clusters:
        # Get new centroid
        if len(clusters[x]) > 0:
            # Get the sum of the cluster
            centroid = sum(clusters[x])
            # commute the mean or centroid
            centroid = centroid/len(clusters[x])
            # Round centroid to 2 decimal get rid of math errors created by abs()
            centroid = round(centroid,3)
            # Update centroid
            centroids[x] = centroid
        # Reset centroid
        centroid = 0

# Algorithm calls
assign_to_clusters(input_cluster_data, clusters, centroids, point_assignments)
update_centroids(input_cluster_data, clusters, centroids)

# Reinitialize the clusters variable to empty lists
clusters = dict(zip(range(num_clusters),[[] for i in range(num_clusters)]))

# Print the point assignments
f1 = open(output_file, 'wb')
for x in point_assignments:
    f1.write(fmt.format(point_assignments[x], print_point_assignments[x]))
f1.close()

# Citation:
"""
https://www.geeksforgeeks.org/python-find-the-closest-key-in-dictionary/
"""