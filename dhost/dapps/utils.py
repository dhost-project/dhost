def get_dapp_type(dapp):
    """Return the available dapp implementation."""
    if hasattr(dapp, "ipfsdapp"):
        return "ipfs"
    return None
