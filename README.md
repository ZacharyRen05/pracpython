# pracpython
2020-01-05 Tutorial

func add(int b, int c) => func add(int b, int c, int d)
.....


int sum = add(1,2);

repository => track all changes


zacharyr47@educbe.ca
ScOOl.@Col123

Use Git or checkout with SVN using the web URL.
https://github.com/ZacharyRen05/pracpython.git

D:\Train>git clone https://github.com/ZacharyRen05/pracpython.git
Cloning into 'pracpython'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.

D:\Train\pracpython>git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        example1.py

nothing added to commit but untracked files present (use "git add" to track)

D:\Train\pracpython>git add . => add all changes to github or gitlab from my current folder

D:\Train\pracpython>git commit -m "Initialize" => file change sets have been committed
[master e7e5393] Initialize
 2 files changed, 34 insertions(+)
 create mode 100644 example1.py
 create mode 100644 subfolder/example2.py

https://stackoverflow.com/questions/38637876/how-do-i-change-switch-user-credentials-used-by-git-command-line-windows-10-g

D:\Train\pracpython>git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 495 bytes | 495.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0)
To https://github.com/ZacharyRen05/pracpython.git
   794bfa9..e7e5393  master -> master
