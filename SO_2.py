import git
for url in urls:
    git.Git("./").clone("git://gitorious.org/git-python/mainline.git")

import shutil
shutil.make_archive(output_filename, 'zip', dir_name_cloned)