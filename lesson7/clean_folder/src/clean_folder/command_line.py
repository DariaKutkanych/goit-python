import sys

from clean_folder.clean import doc_types, create_sorted_folders, sort_docs


def main():

    if len(sys.argv) > 1:

        create_sorted_folders(sys.argv[1])
        sort_docs(sys.argv[1])

    else:

        path_to_garbage = input("Please enter your folder path: ")
        create_sorted_folders(path_to_garbage)
        sort_docs(path_to_garbage)

    print(list(doc_types))
