"""
Programmer: Jarret Angbazo
Created: Feb 07, 2025
Description: Code to initiate new data science project.
"""
import os
import subprocess
import argparse


def create_project_structure(project_name):
    """
    Create Project Structure

    Potential improvements: 
    Remove 'base_dir' hard code and make definition more flexible
    Make 'base_dir' a global so that I can more succinctly recall in later parts of the script  
    """
    base_dir = f"/Users/jarretangbazo/Desktop/Python_Automation/{project_name}"
    
    # Create main project folder
    os.makedirs(base_dir, exist_ok=True)
    
    # Create subfolders
    subdirs = [
        'data/raw', 
        'data/clean',
        'code/R',
        'code/Python',
        'notebooks',
        'reports',
        'models'
        ]
    for subdir in subdirs:
        os.makedirs(os.path.join(base_dir, subdir), exist_ok=True)

    
    # Create README.md
    with open(os.path.join(base_dir, 'README.md'), 'w') as f:
        f.write(f"# {project_name}\n\nData Science project created with automation script.")

def create_virtual_environment(project_name):
    """
    Create Virtual Environment

    Potential Improvements: 
    Make 'base_dir' a global so I don't have to hard code here
    """
    base_dir = f"/Users/jarretangbazo/Desktop/Python_Automation/{project_name}"
    env_name = f"{project_name}_env"
    
    # Create Conda environment with Python and R
    subprocess.run(['conda', 'create', '-n', env_name, 'python=3.9', 'r-essentials', 'r-base', '-y'])
    
    # Activate environment and install essential packages
    activate_cmd = f"conda activate {env_name} && "
    subprocess.run(activate_cmd + "pip install pandas numpy matplotlib scikit-learn jupyter", shell=True)
    subprocess.run(activate_cmd + "Rscript -e \"install.packages(c('tidyverse', 'ggplot2'), repos='http://cran.rstudio.com/')\"", shell=True)
    
    # Create a requirements.txt file to list project dependencies
    subprocess.run(activate_cmd + f"pip freeze > {os.path.join(base_dir, 'requirements.txt')}", shell=True)

def initialize_git(project_name):
    base_dir = f"/Users/jarretangbazo/Desktop/Python_Automation/{project_name}"
    
    # Initialize Git repository
    subprocess.run(['git', 'init'], cwd=base_dir)
    
    # Create .gitignore file
    gitignore_content = """
    # Python
    __pycache__/
    *.py[cod]
    *.so

    # R
    .Rhistory
    .RData
    .Rproj.user/

    # Jupyter Notebooks
    .ipynb_checkpoints

    # VS Code
    .vscode/

    # Environment
    .env
    """
    
    with open(os.path.join(base_dir, '.gitignore'), 'w') as f:
        f.write(gitignore_content.strip())
    
    # Make initial commit
    subprocess.run(['git', 'add', '.'], cwd=base_dir)
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=base_dir)

def main():
    parser = argparse.ArgumentParser(description="Create a new data science project structure.")
    parser.add_argument("project_name", help="Name of the project")
    args = parser.parse_args()

    project_name = args.project_name

    print(f"Creating project structure for {project_name}...")
    create_project_structure(project_name)
    
    print("Creating virtual environment...")
    create_virtual_environment(project_name)
    
    print("Initializing Git repository...")
    initialize_git(project_name)
    
    print(f"Project {project_name} has been created successfully!")

if __name__ == "__main__":
    main()
