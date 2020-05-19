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
#print("input_file: ", input_file)
#print("output_file: ", output_file)
#print("num_clusters: ", num_clusters)

# Read file
input_cluster_data = [float(x.rstrip()) for x in open(input_file)]

# Tester Code to be deleted
#print(input_cluster_data[0:])

# Initialize variables for  centroids, clusters, and point assignments
centroids = dict(zip(range(num_clusters),input_cluster_data[0:num_clusters]))
clusters = dict(zip(range(num_clusters),[[] for i in range(num_clusters)]))

# Tester Code to be deleted
#print("centroids: ",centroids)
#print("clusters: ",clusters)

# create and initialize a dict for mapping points in a cluster
point_assignments = {0: 1.2, 1: 3.6, 2: 5.0, 3: 5.0, 4: 7.6, 5: 10.0, 6: 3.7}

# Tester Code to be deleted
#print("point_assignments: ",point_assignments)

# -create a variable to store old point assignments (from previous iteration)
old_point_assignments = {}

# Save current point assignment into old point assignment variable (create a new dict from current assignment variable)
old_point_assignments = point_assignments

# Tester Code to be deleted
#print("old_point_assignments: ",old_point_assignments)

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
        # Tester Code to be deleted        
        #print("The closest centroid to ", x, point_assignments[x], " is ", closest_index, centroids[closest_index])
        # Add point to the list of points for that cluster
        clusters[closest_index].append(point_assignments[idx])
        # Reset centroid comparator
        centroid_comparator = 100
            
        




#  Update the locations of centroids of the k clusters (make a function for this also)TODO
assign_to_clusters(input_cluster_data, clusters, centroids, point_assignments)
# Reinitialize the clusters variable to empty lists TODO
# clusters = dict(zip(range(k),[[] for i in range(k)]))

# Print the point assignments
# print(point_assignments[0:])
print("Clusters: ", clusters)


# Citation:
"""
https://www.geeksforgeeks.org/python-find-the-closest-key-in-dictionary/
"""