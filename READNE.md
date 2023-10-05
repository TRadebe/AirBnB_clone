# AirBnB Clone Deployment Project

## Learning Objectives
At the end of this project, you should be able to explain:

### General
- What Fabric is and how to use it for code deployment.
- How to create .tgz archives and their significance.
- Execution of Fabric commands locally and remotely.
- File transfer using Fabric.
- Nginx configuration management.
- Difference between root and alias in an Nginx configuration.

## Copyright - Plagiarism
Original work is required to meet learning objectives. Plagiarism is strictly forbidden.

## Requirements

### Python Scripts
- Python scripts should follow PEP 8 style (version 1.7.*).
- Fabric file must work with Fabric 3 version 1.14.post1.
- All files must be executable.
- Documentation for functions and classes is mandatory.

### Bash Scripts
- Bash scripts should be executable and pass Shellcheck.
- Documentation for scripts is required.

### Install Fabric for Python 3 - version 1.14.post1
Use the provided installation instructions to set up Fabric for Python 3.

## Tasks

### 0. Prepare your web servers
Bash script to set up web servers for web_static deployment. It installs Nginx, creates necessary folders, a fake HTML file, 
and updates Nginx configuration.

### 1. Compress before sending
Fabric script to generate a .tgz archive from the web_static folder of the AirBnB Clone repo using the do_pack function.

### 2. Deploy archive!
Fabric script (based on 1-pack_web_static.py) to distribute an archive to web servers using the do_deploy function.

### 3. Full deployment
Fabric script (based on 2-do_deploy_web_static.py) to create and distribute an archive to web servers using the deploy function.

### 4. Keep it clean!
Fabric script (based on 3-deploy_web_static.py) to delete out-of-date archives using the do_clean function.

### 5. Puppet for setup
Redo Task 0 using Puppet for setup.

[GitHub repository: AirBnB_clone_v2](link-to-repository)
Files: 0-setup_web_static.sh, 1-pack_web_static.py, 2-do_deploy_web_static.py, 3-deploy_web_static.py, 100-clean_web_static.py, 
101-setup_web_static.pp
