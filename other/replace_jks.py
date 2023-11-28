import os
import shutil

# Define the name of the file to be replaced
old_file = "etcchosted-test-self-sign.jks"

# Define the name of the new file to replace with
new_file_path = "C:/tmp/etcchosted.test-new.jks"

# Loop through all the subfolders in the current directory
for root, dirs, files in os.walk(
    "C:/drive-d/projects/etcc/company/CICD/ritehorizon-ci-cd-admin/ci-cd-ansible-playbook/inventories"
):
    # print(f"loop {root} with {dirs}")
    # Check if the old file exists in the current subfolder
    if old_file in files:
        # Get the full path of the old file
        old_path = os.path.join(root, old_file)
        # Get the full path of the new file
        # new_path = os.path.join(root, new_file)
        # Replace the old file with the new file
        shutil.copy(new_file_path, old_path)
        # Print a message to indicate the replacement
        print(f"Replaced {old_path} with {new_file_path}")
