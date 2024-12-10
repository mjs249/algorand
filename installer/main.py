from .node_installer import install_node
from .dependency_manager import check_dependencies

def main():
    print("Starting the Algorand installer...")
    check_dependencies()
    install_node()

if __name__ == "__main__":
    main()

