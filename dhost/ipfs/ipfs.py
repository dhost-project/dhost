"""IPFS HTTP API wrapper."""
import json
from typing import Any, Dict, List, Optional

import requests
from django.conf import settings


def remove_empty_dict_values(dic):
    return {k: v for k, v in dic.items() if v}


def clean_dict_values(dic):
    for key, value in dic.items():

        if type(value) == bool:
            # convert a boolean to a string
            # True -> "true" and False -> "false"
            dic[key] = str(value).lower()

        elif type(value) == list:
            # convert a list to a comma separated list as a string
            dic[key] = ",".join([str(i) for i in value])

    return dic


def clean_data(data):
    """Clean requests params removing empty values."""
    if data:
        return remove_empty_dict_values(data)
    return None


def clean_params(params):
    """Clean requests params removing empty values."""
    if not params:
        return None
    params = remove_empty_dict_values(params)
    params = clean_dict_values(params)
    return params


class CLUSTERIPFSAPI:
    BASE_URL = settings.IPFS_CLUSTER_API_URL

    def __init__(self, fail_silently: bool = False) -> None:
        self.fail_silently = fail_silently

    def _get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Any:
        r = requests.get(
            url=self.BASE_URL + path,
            params=clean_params(params),
            headers=clean_params(headers),
            **kwargs,
        )

        if r.status_code == 200:
            return r.json()
        elif not self.fail_silently:
            self._fail(r)
        return None

    def _post(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Any:
        r = requests.post(
            url=self.BASE_URL + path,
            params=clean_params(params),
            headers=clean_params(headers),
            **kwargs,
        )
        if r.status_code == 200:
            try:
                return r.json()
            except json.decoder.JSONDecodeError:
                return r.content.decode()
        elif not self.fail_silently:
            self._fail(r)
        return None

    def _delete(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Any:
        r = requests.delete(
            url=self.BASE_URL + path,
            params=clean_params(params),
            headers=clean_params(headers),
            **kwargs,
        )
        if r.status_code == 200:
            try:
                return r.json()
            except json.decoder.JSONDecodeError:
                return r.content.decode()
        elif not self.fail_silently:
            self._fail(r)
        return None

    def _fail(self, r):
        raise Exception(f"{r.status_code} {r.content.decode()}")

    """Cluster version"""

    def getVersion(self, number=None, commit=None, repo=None, all=None):
        return self._post(
            "version",
            params={
                "number": number,
                "commit": commit,
                "repo": repo,
                "all": all,
            },
        )

    """"Cluster peers"""

    def getPeers(self):
        return self._get("peers")

    """Cluster peer information"""

    def getPeerInformation(self):
        return self._get("id")

    def _add(
        self,
        quiet=None,
        quieter=None,
        silent=None,
        progress=None,
        trickle=None,
        only_hash=None,
        wrap_with_directory=None,
        chunker=None,
        size_262144=None,
        pin=None,
        raw_leaves=None,
        nocopy=None,
        fscache=None,
        cid_version=None,
        hash=None,
        inline=None,
        inline_limit=None,
        **kwargs,
    ):
        return self._post(
            "add",
            params={
                "quiet": quiet,
                "quieter": quieter,
                "silent": silent,
                "progress": progress,
                "trickle": trickle,
                "only-hash": only_hash,
                "wrap-with-directory": wrap_with_directory,
                "chunker": chunker,
                "size-262144": size_262144,
                "pin": pin,
                "raw-leaves": raw_leaves,
                "nocopy": nocopy,
                "fscache": fscache,
                "cid-version": cid_version,
                "hash": hash,
                "inline": inline,
                "inline-limit": inline_limit,
            },
            **kwargs,
        )

    """Add content to the cluster"""

    def add(self, file_path="LICENSE"):
        files = {"file": (file_path, open(file_path, "rb"))}
        return self._add(files=files)

    """List of pins and their allocations (pinset)"""

    def getPinsAndAllocations(self):
        return self._get("allocations")

    """Show a single pin and its allocations (from the pinset)"""

    def getPinsAndAllocationsByCID(self, CID):
        return self._get("allocations/" + CID)

    """Local status of all tracked CIDs"""

    def getlocalStatusAllTrackedCID(self):
        return self._get("pins")

    """Local status of single CID"""

    def getlocalStatusByCID(self, CID):
        return self._get("pins/" + CID)

    """Pin a CID"""

    def pinCID(self, CID):
        return self._post("pins/" + CID)

    """Unpin a CID"""

    def unpinCID(self, CID):
        return self._delete("pins/" + CID)
