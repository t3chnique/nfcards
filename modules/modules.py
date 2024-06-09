def hello():
    return "Hello, World!"


def content():
    return '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            '''


def file_size():
    # Define the maximum allowed file size in bytes (e.g., 10 MB)
    MAX_FILE_SIZE_BYTES = 1000 * 1024 * 1024  # 1 GB
    # Define the maximum allowed total folder size in bytes (e.g., 100 MB)
    MAX_FOLDER_SIZE_BYTES = 10000 * 1024 * 1024  # 10 GB
