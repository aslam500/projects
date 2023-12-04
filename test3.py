
import subprocess


def add_comments_before_commit():
    """
    Checks for staged files and adds comments to them if necessary.

    This function uses `git diff` and an external tool called `Comment`
    to analyze the code and automatically add comments where needed.

    - It retrieves a list of staged files using `git diff` with subprocess.
    - It prints the list of files for debugging/information.
    - It iterates through each file and calls the `add_comments` function.
    """
    # Get a list of staged files using git diff with subprocess
    changed_files = (
        subprocess.check_output(["git", "diff", "--name-only", "--cached"])
        .decode("utf-8")
        .splitlines()
    )

    print(f"Checking these changed files: {changed_files}")  # Print files for debugging/information

    # Loop through each file and add comments
    for file_path in changed_files:
        add_comments(file_path)


def add_comments(file_path):
    """
    Adds comments to a specific file if it needs them.

    This function uses an external tool (e.g., lintr) to generate comments
    and checks its exit code to determine success.

    - It takes a file path as input.
    - It calls the `Comment` tool on the file and receives the output and status code.
    - If the status code indicates success, it writes the generated comments (skipping the first line) to the file.
    - Otherwise, it prints a message indicating no changes are needed.
    """
    answer, status = Comment(file_path)
    if status:
        print(f"Adding comments to {file_path}")
        with open(file_path, "w") as f:
            # Write only actual comments, skipping the first line (likely header)
            for i in range(1, len(answer)):
                f.write(answer[i] + "\n")
    else:
        print(f"No changes needed for {file_path}")


if __name__ == "__main__":
    add_comments_before_commit() ## calling the function

