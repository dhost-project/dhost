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
            # convert a list to a string
            # ["k", "itchenette", "1", 3] ->  "k,itchenette,1,3"
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


class IPFSAPI:
    BASE_URL = settings.IPFS_HTTP_API_URL

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
            return r.json()
        elif not self.fail_silently:
            self._fail(r)
        return None

    def _fail(self, r):
        raise Exception(f"{r.status_code} {r.content.decode()}")

    def get_swarm_peers(self):
        return self._post("v0/swarm/peers")

    def _add(
        self,
        path,
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
            "v0/add",
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
            headers = {
                "path": path
            },
            **kwargs,
        )

    def add_form_data(self, form_data):
        return self._add(path=None, files={"file": form_data})

    def cat(self, arg, offset=None, length=None):
        return self._post(
            "v0/cat",
            params={
                "arg": arg,
                "offset": offset,
                "length": length,
            },
        )

    def version(self, number=None, commit=None, repo=None, all=None):
        return self._post(
            "v0/version",
            params={
                "number": number,
                "commit": commit,
                "repo": repo,
                "all": all,
            },
        )
