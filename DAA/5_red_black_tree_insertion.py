# 5) Insertion in Red-Black Tree

# Node is stored as a dictionary to keep code simple.


def create_node(key):
    return {"key": key, "color": "R", "left": None, "right": None, "parent": None}


def left_rotate(root, x):
    y = x["right"]
    x["right"] = y["left"]
    if y["left"] is not None:
        y["left"]["parent"] = x
    y["parent"] = x["parent"]
    if x["parent"] is None:
        root = y
    elif x == x["parent"]["left"]:
        x["parent"]["left"] = y
    else:
        x["parent"]["right"] = y
    y["left"] = x
    x["parent"] = y
    return root


def right_rotate(root, y):
    x = y["left"]
    y["left"] = x["right"]
    if x["right"] is not None:
        x["right"]["parent"] = y
    x["parent"] = y["parent"]
    if y["parent"] is None:
        root = x
    elif y == y["parent"]["left"]:
        y["parent"]["left"] = x
    else:
        y["parent"]["right"] = x
    x["right"] = y
    y["parent"] = x
    return root


def insert_bst(root, z):
    y = None
    x = root
    while x is not None:
        y = x
        if z["key"] < x["key"]:
            x = x["left"]
        else:
            x = x["right"]
    z["parent"] = y
    if y is None:
        root = z
    elif z["key"] < y["key"]:
        y["left"] = z
    else:
        y["right"] = z
    return root


def fix_insert(root, z):
    while z != root and z["parent"] is not None and z["parent"]["color"] == "R":
        if z["parent"] == z["parent"]["parent"]["left"]:
            y = z["parent"]["parent"]["right"]
            if y is not None and y["color"] == "R":
                z["parent"]["color"] = "B"
                y["color"] = "B"
                z["parent"]["parent"]["color"] = "R"
                z = z["parent"]["parent"]
            else:
                if z == z["parent"]["right"]:
                    z = z["parent"]
                    root = left_rotate(root, z)
                z["parent"]["color"] = "B"
                z["parent"]["parent"]["color"] = "R"
                root = right_rotate(root, z["parent"]["parent"])
        else:
            y = z["parent"]["parent"]["left"]
            if y is not None and y["color"] == "R":
                z["parent"]["color"] = "B"
                y["color"] = "B"
                z["parent"]["parent"]["color"] = "R"
                z = z["parent"]["parent"]
            else:
                if z == z["parent"]["left"]:
                    z = z["parent"]
                    root = right_rotate(root, z)
                z["parent"]["color"] = "B"
                z["parent"]["parent"]["color"] = "R"
                root = left_rotate(root, z["parent"]["parent"])
    root["color"] = "B"
    return root


def insert_rb(root, key):
    node = create_node(key)
    root = insert_bst(root, node)
    root = fix_insert(root, node)
    return root


def inorder(root):
    if root is not None:
        inorder(root["left"])
        print(str(root["key"]) + "(" + root["color"] + ")", end=" ")
        inorder(root["right"])


values = [10, 20, 30, 15, 25, 5]
root = None

print("Insertion order:", values)
for v in values:
    root = insert_rb(root, v)
    print("Inserted", v)

print("Inorder traversal with color (R/B):")
inorder(root)
print()
