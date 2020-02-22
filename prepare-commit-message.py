import os
import sys

try:
    # get commit message file name
    commit_message_file_name = os.environ['COMMIT_MSG_FILE1']

    # open commit message file and read commit message
    commit_message_file = open(commit_message_file_name, 'r')
    data = commit_message_file.read()
    commit_message_file.close()

    # add branch name before commit message
    data = os.getenv('BRANCH_NAME') + ". " + data

    # overwrite commit message file
    commit_message_file = open(commit_message_file_name, "w")
    commit_message_file.write(data)
    commit_message_file.close()
except Exception as err:
    print("Prepare commit message script (.git/hooks/prepare-commit-msg) error: " + str(err))
    sys.exit(1)
