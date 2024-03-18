<!-- FILE DESCRIPTION -->
<!-- template.py
    create a python script that creates a default project file structure
    
    ".github/workflows/.gitkeep" 
    .github is the directory for github to store and track git specific templates and configurations files (YAML)

    for CI/CD through github Actions     
    .gitkeep file is to track the directory it is in-->

<!--
os.makedirs(filedir, exist_ok=True) , here exists_ok commands to create the folder recursively. So it can help us to create folders inside alredy existing folders (Tree)
 -->