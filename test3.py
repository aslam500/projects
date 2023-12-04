def add_comments_before_commit():
    changed_files = subprocess.check_output(['git', 'diff', '--name-only', '--cached']).decode('utf-8').splitlines()
    print(changed_files)

    for file_path in changed_files:
        add_comments(file_path)

def add_comments(file_path):
    answer, status = Comment(file_path)
    if status:
        with open(file_path, 'w') as f:
            for i in range(1, len(answer)):
                f.write(answer[i] + "\n")

        
    else:
        print(f"no changes found {file_path}")


   
if __name__ == '__main__':
    # local_ref, local_sha, remote_ref, remote_sha = sys.stdin.read().strip().split()

    # add_comments_before_push(local_ref, local_sha, remote_ref, remote_sha)
    add_comments_before_commit()
