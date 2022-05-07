""" Tree lab, CSCI 204 """
import pickle

def play(node):
    """ Play the Animal Game from the given node. """
    # Your code goes here. You may write additional methods as needed.
    if node.left == None and node.right == None: # condition for leaf
        # guess = input('Is your animal a', node,'?')
        s = 'Is your animal a ' + node.data + '? '
        guess = input(s)
        debug = is_yes(guess)
        
        if debug: # if guess is correct
            print('Congratulations!')
            print("Thank you for playing.")
            
        else: 
            print('Oh no! I guessed wrong!')
            new_animal = input('What animal were you thinking of? ')
            s = 'What question should I have asked to tell your ' + new_animal + ' and my ' + node.data + ' apart? '
            debug_quest = input(s)
            # create a new pair of leaf 
            node.right = Node(node.data)
            node.left = Node(new_animal)
            node.data = debug_quest       
            
    else:
        question = str(node.data) + ' '
        response = input(question)
        if is_yes(response) == True:
            play(node.right)
        else:
            play(node.left)
    return '' 

def is_yes(response):
    """ Was this a yes response? """
    return response=="yes" or response=="y" or response=="Yes" or response=="Y"

def main():
    """ Run the Animal Game. """
    # See if they want to print the tree.
    debugMode = input("Print the tree as you play? ")
    debug = is_yes(debugMode)

    # Assemble the initial tree
    root = Node("Does it have feathers?")
    left = Node("tiger")
    right = Node("chicken")
    root.left = left
    root.right = right

    while True:
        print("Think of an animal.")
        play(root)
        if debug:
            root.print()
            print()
        response = input("Play again? ")
        if not is_yes(response): break
    
    tree = root
    store_data(tree, 'animal tree')
    load_data()
    
def store_data(bin_tree, name):
    data_base = {}
    data_base[name] = bin_tree
    dbfile = open('animal_tree', 'ab') 
    pickle.dump(data_base, dbfile)
    dbfile.close()
    
def load_data():
    dbfile = open('animal_tree', 'rb')
    data_base = pickle.load(dbfile)
    for keys in data_base:
        print(keys, '=>', data_base[keys])
    dbfile.close()

class Node:
    def __init__(self, data):
        """ Initialize a binary tree node with given data. The left and right
            branches are set to None (null). """
        self.data = data
        self.left = None
        self.right = None

    def print(self):
        """ Print out the tree rooted at this node. """
        lines = []
        strings = []
        self.print_nodes(lines, strings)
        st = ""
        for string in strings:
            st = st + string
        print(st)

    def print_nodes(self, lines, strings):
        """ Helper function for print(). """
        level = len(lines)
        if self.right != None:
            lines.append(False)
            self.print_lines(lines, strings, "\n")
            self.right.print_nodes(lines, strings)
            lines.pop(level)
        else:
            self.print_lines(lines, strings, "\n")

        if level>0:
            old = lines.pop(level-1)
            self.print_lines(lines, strings, "  +--")
            lines.append(not old)
        strings.append(self.data + "\n")

        if self.left != None:
            lines.append(True)
            self.left.print_nodes(lines, strings)
            self.print_lines(lines, strings, "\n")
            lines.pop(level)
        else:
            self.print_lines(lines, strings, "\n")

    def print_lines(self, lines, strings, suffix):
        """ Helper function for print(). """
        for line in lines:
            if line: strings.append("  |  ")
            else:    strings.append("     ")
        strings.append(suffix)

main()
