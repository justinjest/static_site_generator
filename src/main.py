from textnode import TextNode


def main():
    textnode = TextNode("This is a test node", "bold", "https://www.boot.dev")
    print(textnode.__repr__())
if __name__ == "__main__":
    main()