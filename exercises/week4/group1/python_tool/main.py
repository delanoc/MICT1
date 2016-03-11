# #################################################################################################################### #
# Tool:                 A tool to split a data file into clusters of its own cluster size.               #
# Students and group:   Group 1 - Delano Corvers, Rik Kierkels and Davy Heutmekers.                                    #
# Assignment:           Exercises Week 4                                                                               #
# Module:               MICT1 - Reverse Data Engineering                                                               #
# #################################################################################################################### #
from os import getcwd


# Split the provided data file into clusters of 4096 bytes.
def cluster_splitter(cluster_size=4096):
    file_path = getcwd() + r"\files\data"

    with open(file_path, "rb") as f:
        cluster_counter = 1

        seeker = 0
        f.seek(seeker)
        index = f.read(cluster_size)

        while index != "":
            create_cluster_file(index, cluster_counter)
            cluster_counter += 1
            seeker += cluster_size

            # Get ready to process the next 4096 byte cluster.
            f.seek(seeker)
            index = f.read(cluster_size)


# Write each discovered cluster to a new file.
def create_cluster_file(array, counter):
    file_path = getcwd() + r"\files\clusters\cluster_"

    with open(file_path + str(counter), "wb") as f:
        f.writelines(array)


# Entry point of the application.
def main():
    print "The tool has started...\n"
    cluster_splitter()
    print "\nFinished running..."


main()
