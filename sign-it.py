import os

def add_signature(file_path, author, signature):
    with open(file_path, 'r') as file:
        content = file.read()

    comment_block = f'''
/*
   Author: {author}
   Signature: {signature}
   Date: {get_current_date()}
*/
'''

    with open(file_path, 'w') as file:
        file.write(comment_block + content)

def get_current_date():
    # You can customize this function to format the date as needed
    import datetime
    return datetime.datetime.now().strftime('%Y-%m-%d')

def add_signature_to_directory(directory_path, author, signature = 'BKA-220205'):
    signature = signature.upper()
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.js') or file_name.endswith('.ts') or file_name.endswith('.tsx') or file_name.endswith('.jsx'):
                file_path = os.path.join(root, file_name)
                add_signature(file_path, author, signature)

# Example usage:
author_name = 'Bernard'
unique_signature = 'BKA-220205'
directory_to_sign = "C:\\Users\\Kirk\\Desktop\\2024"

add_signature_to_directory(directory_to_sign, author_name, unique_signature)
