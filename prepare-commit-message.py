print(1)

import os
print(2)
import sys
print(3)
try:
    # get commit message file name
    commit_message_file_name = os.environ['COMMIT_MSG_FILE']

    # open commit message file and read commit message
    commit_message_file = open(commit_message_file_name, 'r')
    data = commit_message_file.read()
    commit_message_file.close()

    # add branch name before commit message
    data = op.getenv('BRANCH_NAME') + ". " + data

    # overwrite commit message file
    commit_message_file = open(commit_message_file_name, "w")
    commit_message_file.write(data)
    commit_message_file.close()
except KeyError:
    print("Error!!!")
    sys.exit(1)
