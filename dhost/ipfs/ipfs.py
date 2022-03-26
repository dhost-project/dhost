"""IPFS HTTP API wrapper."""
import json
import os
from typing import Any, Dict, Optional

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


class ClusterIPFSAPI:
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
                return r.content
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
                return r.content
        elif not self.fail_silently:
            self._fail(r)
        return None

    def _fail(self, r):
        raise Exception(f"{r.status_code} {r.content.decode()}")

    def get_version(self, number=None, commit=None, repo=None, all=None):
        """Cluster version"""
        return self._post(
            "version",
            params={
                "number": number,
                "commit": commit,
                "repo": repo,
                "all": all,
            },
        )

    def get_peers(self):
        """ "Cluster peers"""
        return self._get("peers")

    def get_peer_info(self):
        """Cluster peer information"""
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

    def add(self, url):
        """Add content to the cluster"""
        multiple_files = {}
        index = 0

        for path, subdirs, files in os.walk(url):
            for name in files:
                index += 1
                multiple_files["file" + str(index)] = (
                    (os.path.join(path, name)),
                    (open((os.path.join(path, name)), "rb")),
                )

        return self._add(files=multiple_files)

    def get_pins_and_allocations(self):
        """List of pins and their allocations (pinset)"""
        return self._get("allocations")

    def get_pins_and_allocations_by_cid(self, CID):
        """Show a single pin and its allocations (from the pinset)"""
        return self._get("allocations/" + CID)

    def get_local_status_all_tracked_cid(self):
        """Local status of all tracked CIDs"""
        return self._get("pins")

    def get_local_status_by_cid(self, CID):
        """Local status of single CID"""
        return self._get("pins/" + CID)

    def pin_cid(self, CID):
        """Pin a CID"""
        return self._post("pins/" + CID)

    def unpin_cid(self, CID):
        """Unpin a CID"""
        return self._delete("pins/" + CID)
