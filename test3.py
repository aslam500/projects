
import subprocess


def add_comments_before_commit():
    """Checks for staged files and adds comments to them if necessary."""
    # Get a list of staged files using git diff
    changed_files = subprocess.check_output(
        ["git", "diff", "--name-only", "--cached"]
    )
    .decode("utf-8")
    .splitlines()

    print(f"Checking these changed files: {changed_files}")

    # Loop through each file and add comments
    for file_path in changed_files:
        add_comments(file_path)


def add_comments(file_path):
    """Adds comments to a specific file if it needs them."""
    # Use an external tool (Comment) to generate comments and check its status
    answer, status = Comment(file_path)
    if status:
        print(f"Adding comments to {file_path}")
        with open(file_path, "w") as f:
            # Write all generated comments except the first line (likely header)
            for i in range(1, len(answer)):
                f.write(answer[i] + "\n")
    else:
        print(f"No changes needed for {file_path}")


if __name__ == "__main__":
    add_comments_before_commit()


