from dhost.utils.git import get_number_of_commits


def get_version(version_format, last_major_version_hash):
    return version_format.format(get_number_of_commits(last_major_version_hash))
