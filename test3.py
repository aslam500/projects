#import necessary
import re
import subprocess
import os

def add_comments_before_commit():
    changed_files = (
        subprocess.check_output(["git", "diff", "--name-only", "--cached"])
        .decode("utf-8")
        .splitlines()
    )

    for file_path in changed_files:
        add_comments(file_path)


def add_comments(file_path):
    answer, status = Comment(file_path)
    if status:
        with open(file_path, "w") as f:
            for i in range(1, len(answer)):
                f.write(answer[i] + "\n")
    else:
        pass


if __name__ == "__main__":
    add_comments_before_commit() 

