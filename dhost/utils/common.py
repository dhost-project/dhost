import os
import subprocess


def get_number_of_commits(git_hash):
    """Get the total number of commits since last version if specified."""
    with open(os.path.devnull, "w+") as null:
        try:
            number_of_commits = (
                subprocess.Popen(
                    ["git", "rev-list", git_hash + "..HEAD", "--count"],
                    stdout=subprocess.PIPE,
                    stderr=null,
                    stdin=null,
                )
                .communicate()[0]
                .strip()
                .decode("utf-8")
            )
        except (OSError, IOError):
            pass
        if number_of_commits:
            return number_of_commits
    return ""


def generate_version(version_format, git_hash):
    return version_format.format(get_number_of_commits(git_hash))


def get_version():
    from dhost import __version__

    return __version__
