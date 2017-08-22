import os


def launch_analysis(data_file):
	# we get the right path.
    directory = os.path.dirname(os.path.dirname(__file__))
    # with this path, we go inside the folder `data` and get the file.
    path_to_file = os.path.join(directory, "data", data_file) 


    with open(path_to_file,"r") as f:
        preview = f.readline()


    print("Yeah! We managed to read the file. Here is a preview: {}".format(preview))



if __name__ == "__main__":
    launch_analysis('SyceronBrut.xml')

 