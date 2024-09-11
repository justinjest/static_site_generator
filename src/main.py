from textnode import TextNode
import shutil, os
from pathlib import Path

def main():
    # Static folder is one level above and then into static
    if not os.path.exists("static"):
        raise Exception ("No static directory")
    print ("Found static directory")
    public_path = "public"
    static_path = "static"
    empty_folder(public_path)
    copy_static(static_path, public_path)

# Path -> None
# Deletes everything in Path to allow us to create new folders
def empty_folder(path):
    # If public doesn't exist just make it
    if not os.path.exists(path):
        print(f"{path} directory does not exist")
        os.mkdir(path)
        print (f"{path} directory created")
        return
    
    # If public does exist we must empty it out
    print (f"{path} directory exists, must be purged")
    shutil.rmtree(path)
    os.mkdir(path)
    print (f"{path} directory purged")

# None -> None
# Copies all files in ~/static to ~/public
# Should use recursion per design docs
def copy_static(from_path, to_path):
    for item in os.listdir(from_path):
        path = os.path.join(from_path, item)
        if os.path.isfile(path):
            print (f"Moving {path} to {to_path}")
            shutil.copy(path, to_path)
        else:
            new_folder = os.path.join(to_path, item)
            print (f"{path} is a subfolder, moved to {new_folder}")
            os.mkdir(new_folder)
            copy_static(path, new_folder)

if __name__ == "__main__":
    main()