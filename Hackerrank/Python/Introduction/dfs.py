def dfs(root):
    if not root:
        return
    # process root
    dfs(root.left)
    dfs(root.right)
