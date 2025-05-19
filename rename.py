import os

directory = 'models'  # or your target directory

for root, _, files in os.walk(directory):
    for file in files:
        if '_standard_unfair' in file and file.endswith('.pkl'):
            model_name = file.split('_')[0] + '.pkl'
            src = os.path.join(root, file)
            dst = os.path.join(root, model_name)
            os.rename(src, dst)
            print(f"Renamed: {file} -> {model_name}")

