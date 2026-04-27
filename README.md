# git-massclone
Scripts in Bash and Python for cloning multiple Github repositories with a single command in terminal.
-----

**git-massclone** is a collection of scripts written in **Bash** and **Python** to mass clone repositories from Github. Both scripts read a list of Github clone URLs saved in a text file (.TXT) and run the `git clone` command for every URL in the terminal. Both scripts do a check wheter the repository is already cloned or not to prevent cloning a repository many times. 

Both scripts check if **Git** is installed on the system and `git` command is available in the terminal. 

The *Python* script can be run on both *Linux* and *Windows* operating systems (if Python is installed on the Windows machine).

**Note:** If you have private repositories ***make sure*** that you **select** the credential helper of your choice in `git config` **BEFORE** starting the *git-massclone* script. That way you will be able to fill and store your credentials the first time **git** asks for them.

**Note:** The URLs in the file must in format: **https://github.com/ivaylo-vasilev/git-massclone.git**
        
[*] *Please check the contents of the file **iv-public-repos.txt** to see an example of how this list should be created in order for the both scripts to be able to correctly read it.*
