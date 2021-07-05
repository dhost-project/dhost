import os
import subprocess


def get_number_of_commits(last_major_version_hash):
    # return the total number of commits since last version if specified
    with open(os.path.devnull, 'w+') as null:
        try:
            number_of_commits = subprocess.Popen(
                ['git', 'rev-list', last_major_version_hash + '..HEAD', '--count'],
                stdout=subprocess.PIPE,
                stderr=null,
                stdin=null,
            ).communicate()[0].strip().decode('utf-8')
        except (OSError, IOError):
            pass
        if number_of_commits:
            return number_of_commits
    return '0'
