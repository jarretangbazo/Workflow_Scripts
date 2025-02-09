import os
import subprocess
import argparse
import json

def create_project_structure(project_name):
    base_dir = f"/Users/jarretangbazo/Desktop/Python_Automation/{project_name}"
    os.makedirs(base_dir, exist_ok=True)
    subdirs = ['data', 'code', 'notebooks', 'reports', 'models']
    for subdir in subdirs:
        os.makedirs(os.path.join(base_dir, subdir), exist_ok=True)
    with open(os.path.join(base_dir, 'README.md'), 'w') as f:
        f.write(f"# {project_name}\n\nData Science project created with automation script.")

def create_virtual_environment(project_name, languages, packages):
    base_dir = f"/Users/jarretangbazo/Desktop/Python_Automation/{project_name}"
    env_name = f"{project_name}_env"
    
    # Create Conda environment with specified languages
    create_cmd = ['conda', 'create', '-n', env_name, '-y']
    if 'python' in languages:
        create_cmd.extend(['python=3.9'])
    if 'r' in languages:
        create_cmd.extend(['r-essentials', 'r-base'])
    subprocess.run(create_cmd)
    
    # Activate environment and install packages
    activate_cmd = f"source activate {env_name} && "
    for lang, pkg_list in packages.items():
        if lang == 'python' and pkg_list:
            subprocess.run(activate_cmd + f"pip install {' '.join(pkg_list)}", shell=True)
        elif lang == 'r' and pkg_list:
            r_install_cmd = f"install.packages(c({', '.join([f"'{pkg}'" for pkg in pkg_list])}), repos='http://cran.rstudio.com/')"
            subprocess.run(activate_cmd + f"Rscript -e \"{r_install_cmd}\"", shell=True)
    
    # Create a requirements.txt file for Python packages
    if 'python' in languages:
        subprocess.run(activate_cmd + f"pip freeze > {os.path.join(base_dir, 'requirements.txt')}", shell=True)

def initialize_git(project_name):
    base_dir = f"/Users/jarretangbazo/Desktop/Python_Automation/{project_name}"
    subprocess.run(['git', 'init'], cwd=base_dir)
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
    subprocess.run(['git', 'add', '.'], cwd=base_dir)
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=base_dir)

def main():
    parser = argparse.ArgumentParser(description="Create a new data science project structure.")
    parser.add_argument("project_name", help="Name of the project")
    parser.add_argument("--languages", nargs='+', choices=['python', 'r'], default=['python'], help="Programming languages to include")
    parser.add_argument("--packages", type=json.loads, default='{}', help="JSON string of packages to install for each language")
    args = parser.parse_args()

    project_name = args.project_name
    languages = args.languages
    packages = args.packages

    print(f"Creating project structure for {project_name}...")
    create_project_structure(project_name)
    
    print("Creating virtual environment...")
    create_virtual_environment(project_name, languages, packages)
    
    print("Initializing Git repository...")
    initialize_git(project_name)
    
    print(f"Project {project_name} has been created successfully!")

if __name__ == "__main__":
    main()
