# replace_symbol_name.py

def replace_text_in_file(file_path, old_text, new_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        updated_content = content.replace(old_text, new_text)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f'"{old_text}" successfully replaced with "{new_text}" in {file_path}')
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except Exception as e:
        print(f'An error occurred: {e}')

# Kullanım
file_path = '000MCLib.kicad_sym'
replace_text_in_file(file_path, 'CamTracker', '000MCLib')
