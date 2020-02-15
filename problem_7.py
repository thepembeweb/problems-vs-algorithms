from collections import defaultdict
# A RouteTrie will store our routes and their associated handlers


class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.insert("/", handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        path_list = self.split_path(path)
        current_node = self.root
        for path in path_list:
            current_node = current_node.children[path]
        current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        path_list = self.split_path(path)
        current_node = self.root
        for path in path_list:
            if path not in current_node.children:
                return
            current_node = current_node.children[path]
        return current_node.handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = path.split("/")
        path_list[0] = "/"
        if path_list[-1] == "":
            return path_list[:-1]
        return path_list

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.


class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = None


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, nohandler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie(handler)
        self.not_fount = nohandler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path == "" or not isinstance(path, str):
            return "Please input an valid path!"
        self.route.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == "" or not isinstance(path, str):
            return "Please input an valid path!"
        handler = self.route.find(path)
        return handler if handler is not None else self.not_fount


# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me/help", "help handler")

# some lookups with the expected output
print(router.lookup(""))  # should print "Please input an valid path!" message.
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
# should print 'help handler' or None if you did not implement one
print(router.lookup("/home/about/me/help"))
