import urllib.request
import os

def download(file):
    loc = "./dontpush/" + file.split("/")[-1]
    if (not os.path.exists(loc)):
        urllib.request.urlretrieve(file, loc)
    else:
        print("File Already Exists: " + loc)


if not os.path.exists("./dontpush"):
    os.makedirs("./dontpush")

download("https://download1491.mediafire.com/2faroyd5cqzg/tiqdz8qa2qb10oc/UltraStaffChat_Bungeecord-4.0.0.jar")
