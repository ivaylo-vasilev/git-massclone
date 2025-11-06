#!/bin/bash

# Clone multiple github repositories using git
# (c)Ivaylo Vasilev

if [[ "$#" -ne 1 ]]; then
    echo "usage: $0 <git-repos-urls.txt>"
    exit 1
fi

reposurls=$1
if [[ ! -f $reposurls ]]; then
    echo "error: $reposurls does not exist"
    exit 2
fi

repos=()
while IFS= read -r line; do
    repos+=("$line")
done < $reposurls

for repo in "${repos[@]}"
do
    IFS="/" read -r -a urlparts <<< "$repo"
    clonedir="${urlparts[-1]%.*}"
    if [[ ! -d $clonedir ]]; then
        git clone $repo
    else
        echo "$0: repository '$clonedir' already cloned"
    fi
done
