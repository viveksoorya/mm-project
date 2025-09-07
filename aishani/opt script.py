import os
import string

root_dir = "/workspaces/mm-project/aishani"  # base path
output_suffix = "_opt.inp"

# iterate over folders m..y
for folder in string.ascii_lowercase:
    if folder < "m" or folder > "y":
        continue

    folder_path = os.path.join(root_dir, folder, "orca_inputs")
    if not os.path.isdir(folder_path):
        continue

    print(f"Processing folder: {folder_path}")

    for filename in os.listdir(folder_path):
        if filename.endswith(".inp"):
            input_path = os.path.join(folder_path, filename)

            with open(input_path, "r") as f:
                lines = f.readlines()

            # Replace SP with Opt in the first keyword line
            new_lines = []
            for line in lines:
                if line.strip().startswith("!"):
                    new_lines.append(line.replace("SP", "Opt"))
                else:
                    new_lines.append(line)

            # new filename
            output_filename = filename.replace(".inp", output_suffix)
            output_path = os.path.join(folder_path, output_filename)

            with open(output_path, "w") as f:
                f.writelines(new_lines)

            print(f" → Created {output_path}")
