import os


def get_dapp_type(dapp):
    """Return the available dapp implementation."""
    if hasattr(dapp, "ipfsdapp"):
        return "ipfs"
    return None


def create_tree_folder(treeview, path, index):
    for root, dirs, files in os.walk(path):
        if index == 1:
            treeview["child"] = []
            treeview["name"] = os.path.basename(root)
            treeview["id"] = index
            treeview["toggled"] = True

            for d in dirs:
                index += 1
                treeview["child"].append(
                    {
                        "name": d,
                        "id": index,
                        "child": create_tree_folder(
                            {}, os.path.join(root, d), index + 1
                        ),
                    }
                )
            for f in files:
                index += 1
                treeview["child"].append({"name": f, "id": index, "child": []})
        else:
            treeview_tree = []
            for d in dirs:
                index += 1
                treeview_tree.append(
                    {
                        "name": d,
                        "id": index,
                        "child": create_tree_folder(
                            {}, os.path.join(root, d), index + 1
                        ),
                    }
                )
            if len(dirs) <= 0:
                for f in files:
                    index += 1
                    treeview_tree.append({"name": f, "id": index, "child": []})
            return treeview_tree
