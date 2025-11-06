# git-massclone
Scripts in Bash and Python for cloning multiple Github repositories with a single command in terminal.
-----
**git-massclone** is a collection of scripts written in **Bash** and **Python** to mass clone repositories from Github. Both scripts read a list of Github clone URLs saved in a text file (.TXT) and run the `git clone` command for every URL in the terminal. Both scripts do a check wheter the repository is already cloned or not to prevent cloning a repository many times. The *Python* based script checks if **Git** is installed on the system and `git` command is available in the terminal. Also the *Python* script can be run on both *Linux* and *Windows* operating systems (if Python is installed on the Windows machine).
**Note:** The URLs in the file must in format: **https://github.com/ivaylo-vasilev/git-massclone.git**
        Please check the contents of the file **iv-public-repos.txt** to see an example of how this list should be created in order for the both scripts to be able to correctly read it.
