Python script to create a DS project folder and subfolders in /Users/jarretangbazo/Desktop/Python_Automation, set up a conda virtual environment with Python and R, install essential Python/R packages, create documentation files, initialize a Git repository and make initial commit. Note: Conda must be installed prior to running this script.

To run 'create_ds_projects.py'
1. Open Terminal
2. Navigate to folder where script is saved (e.g., cd /Users/jarretangbazo/Desktop/Python_Automation)
3. Make the script executable by typing: chmod +x create_ds_projects.py
4. Run the script (e.g. python create_ds_projects.py project_name)
5. Open the project in VS Code: code /Users/jarretangbazo/Desktop/Python_Automation/project_name
6. Activate the virtual environment: conda activate project_name_env

The program 'create_ds_projects_ADV.py' is more advanced as it allows specifying the languages and programming packages for which you want to set up a virtual environment. 
To run 'create_ds_projects_ADV.py'
1. Open Terminal
2. Navigate to folder where script is saved (e.g., cd /Users/jarretangbazo/Desktop/Python_Automation)
3. Make the script executable by typing: chmod +x create_ds_projects_ADV.py
4. Run the script.
    To create a project with both Python and R:
    python create_ds_project_ADV.py my_project --languages python r --packages '{"python": ["pandas", "numpy", "scikit-learn"], "r": ["tidyverse", "ggplot2"]}'

    To create a project with only Python:
    python create_ds_project.py python_project --languages python --packages '{"python": ["pandas", "numpy", "matplotlib"]}'

    To create a project with only R:
    python create_ds_project.py r_project --languages r --packages '{"r": ["tidyverse", "caret", "randomForest"]}'

    To create a project without specifying packages:
    python create_ds_project.py basic_project --languages python r
5. Open the project in VS Code: code /Users/jarretangbazo/Desktop/Python_Automation/project_name
6. Activate the virtual environment: conda activate project_name_env

Adjust 'create_virtual_environment' function to extend the programming languages the Python script will support.