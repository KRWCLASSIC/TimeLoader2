import os
import subprocess
import shutil
import time
import json
import sys
from colorama import init, Fore, Style

def waitfunc():
    time.sleep(1)

def press_enter_to_continue():
    input("\nPress Enter to continue...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clean_start():
    directory_name = "temp_mods"
    try:
        shutil.rmtree(directory_name, ignore_errors=True)
    except Exception:
        pass

def load_game(game_path):
    clear_screen()
    
    if game_path == "modded_game":
        if check_modded_game_folder():
            print("Modded game found. Starting the game...")
            os.system(f"start {game_path}\\TimeKeeper.exe")
        else:
            print("Modded game not found. Please run and build modded game first.")
    else:
        print(f"Starting the {game_path}...")
        os.system(f"start {game_path}\\TimeKeeper.exe")

    waitfunc()
    clear_screen()


def show_mod_list():
    clear_screen()
    temp_directory = "temp_mods"
    mods_directory = "mods"

    mod_list = [os.path.splitext(mod)[0] for mod in os.listdir(mods_directory) if mod.endswith('.zip')]

    if not mod_list:
        print("No mods found.")
    else:
        for mod in mod_list:
            selected_mod_archive = mod + ".zip"
            mod_folder = os.path.join(temp_directory, selected_mod_archive)
            mod_meta_path = os.path.join(mod_folder, 'modmeta.tkml')

            print(f"\nMod: {selected_mod_archive}")

            if os.path.exists(mod_meta_path):
                with open(mod_meta_path, 'r') as meta_file:
                    mod_data = json.load(meta_file)
                    print(f"\tName: {mod_data.get('mod_name', 'Unknown')}")
                    print(f"\tAuthor: {mod_data.get('author', 'Unknown')}")
                    print(f"\tMod Version: {mod_data['mod_version']}")
                    print(f"\tGame Version: {'Universal' if mod_data['version'] == 'tkml2_frame' else mod_data['version']}")
                    print(f"\tDescription: {mod_data.get('description', 'No description available')}")
                    dependencies = mod_data.get('dependencies')
                    if dependencies:
                        print("\tDependencies:")
                        for dependency in dependencies:
                            print(f"\t\t{dependency}")
            else:
                print("\tNo metadata found.")

    press_enter_to_continue()
    clear_screen()

def check_modded_game_folder():
    return os.path.exists("modded_game")

def extract_mods():
    clear_screen()
    mods_directory = "mods"
    temp_directory = "temp_mods" 

    if os.path.exists(temp_directory):
        shutil.rmtree(temp_directory)

    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory)

    for mod in os.listdir(mods_directory):
        mod_path = os.path.join(mods_directory, mod)
        if mod.endswith('.zip'):
            print(f"Extracting {mod} to {temp_directory}")
            subprocess.run(['utils\\7z', 'x', f'-o{temp_directory}\\{mod}', mod_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    waitfunc()

def display_mod_info():
    clear_screen()
    temp_directory = "temp_mods"
    mods = os.listdir(temp_directory)
    metadata_found = False

    for index, mod_folder in enumerate(mods, start=1):
        mod_meta_path = os.path.join(temp_directory, mod_folder, 'modmeta.tkml')
        if os.path.exists(mod_meta_path):
            with open(mod_meta_path, 'r') as meta_file:
                mod_data = json.load(meta_file)
                print(f"Mod: {mod_folder}\n")
                print(f"\tName: {mod_data['mod_name']}")
                print(f"\tAuthor: {mod_data['author']}")
                print(f"\tMod Version: {mod_data['mod_version']}")
                print(f"\tGame Version: {'Universal' if mod_data['version'] == 'tkml2_frame' else mod_data['version']}")
                print(f"\tDescription: {mod_data['description']}")
                if mod_data.get('dependencies'):
                    print(f"\tDependencies:")
                    for dependency in mod_data['dependencies']:
                        print(f"\t\t{dependency}")
                if index != len(mods):
                    print("\n====================================================\n")
            metadata_found = True

    if not metadata_found:
        print("No mod metadata was found because of possible mod files issue.")
        press_enter_to_continue()
    
    waitfunc()
    waitfunc()

def check_mod_ids():
    clear_screen()
    print("Checking Mod ID's...")
    temp_directory = "temp_mods"
    folders_to_remove = []

    for mod_folder in os.listdir(temp_directory):
        mod_meta_path = os.path.join(temp_directory, mod_folder, 'modmeta.tkml')
        if os.path.exists(mod_meta_path):
            try:
                with open(mod_meta_path, 'r') as meta_file:
                    mod_data = json.load(meta_file)
                    if 'mod_id' not in mod_data:
                        print(f"No mod ID found for mod '{mod_data.get('mod_name')}' in folder '{mod_folder}'. Adding this mod to the removal queue.")
                        folders_to_remove.append(mod_folder)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in '{mod_meta_path}': {e}")
                press_enter_to_continue()
                sys.exit("Exiting due to JSON decoding error.")

    for folder in folders_to_remove:
        shutil.rmtree(os.path.join(temp_directory, folder), ignore_errors=True)
        print(f"Mod '{folder}' successfully removed.")
        press_enter_to_continue()
    waitfunc()

def check_conflicting_mod_ids():
    clear_screen()
    print("Checking for conflicting Mod IDs...")
    temp_directory = "temp_mods"
    mod_ids = {}
    folders_to_remove = []

    for mod_folder in os.listdir(temp_directory):
        mod_meta_path = os.path.join(temp_directory, mod_folder, 'modmeta.tkml')
        if os.path.exists(mod_meta_path):
            with open(mod_meta_path, 'r') as meta_file:
                mod_data = json.load(meta_file)
                mod_id = mod_data.get('mod_id')
                if mod_id:
                    if mod_id in mod_ids:
                        print(f"Conflicting mod ID '{mod_id}' found between mods '{mod_folder}' and '{mod_ids[mod_id]}'. Adding these mods to the removal queue.")
                        folders_to_remove.extend([mod_folder, mod_ids[mod_id]])
                    else:
                        mod_ids[mod_id] = mod_folder

    for folder in folders_to_remove:
        shutil.rmtree(os.path.join(temp_directory, folder), ignore_errors=True)
        print(f"Mod '{folder}' removed due to conflicting mod ID.")

    if folders_to_remove:
        print("\nConflicting mods have been successfully removed.")
        press_enter_to_continue()
    waitfunc()

def check_mod_files():
    clear_screen()
    print("Checking if necessary Mod files exist...")
    temp_directory = "temp_mods"
    mods = os.listdir(temp_directory)
    missing_files = False
    folders_to_remove = []

    for mod_folder in mods:
        mod_meta_path = os.path.join(temp_directory, mod_folder, 'modmeta.tkml')
        auto_apply_path = os.path.join(temp_directory, mod_folder, 'autoapply.tkml')
        
        if not os.path.exists(mod_meta_path):
            print(f"Missing 'modmeta.tkml' for mod: {mod_folder}")
            missing_files = True
            folders_to_remove.append(mod_folder)

        if not os.path.exists(auto_apply_path):
            print(f"Missing 'autoapply.tkml' for mod: {mod_folder}")
            missing_files = True
            folders_to_remove.append(mod_folder)

    if missing_files:
        print("Some necessary mod files are missing. Removing affected mod folders...")
        for folder in folders_to_remove:
            shutil.rmtree(os.path.join(temp_directory, folder), ignore_errors=True)
            print(f"Mod folder '{folder}' removed due to missing files.")
        
        press_enter_to_continue()
    else:
        print("All necessary mod files exist.")
    
    waitfunc()

def create_modded_instance():
    clear_screen()
    print("Creating modded instance of a game.")
    base_game_path = "basegame"
    modded_game_path = "modded_game"

    if os.path.exists(modded_game_path):
        try:
            shutil.rmtree(modded_game_path)
            print("Existing modded game instance removed.")
        except Exception as e:
            print(f"Error removing existing modded game folder: {e}")
            press_enter_to_continue()
            pass

    try:
        shutil.copytree(base_game_path, modded_game_path)
        print("Modded instance of a game created.")
    except FileNotFoundError:
        print("Base game folder not found.")
        press_enter_to_continue()
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
        press_enter_to_continue()
        pass
    waitfunc()
    waitfunc()
    clear_screen()

def apply_mods():
    temp_mods_directory = "temp_mods"
    modded_game_directory = os.path.join(os.getcwd(), "modded_game")

    for mod_folder in os.listdir(temp_mods_directory):
        mod_folder_path = os.path.join(temp_mods_directory, mod_folder)
        autoapply_path = os.path.join(mod_folder_path, 'autoapply.tkml')

        if os.path.isdir(mod_folder_path) and os.path.exists(autoapply_path):
            with open(autoapply_path, 'r') as autoapply_file:
                try:
                    mod_data = json.load(autoapply_file)
                    mod_files = mod_data.get('mod_files')

                    if mod_files:
                        for mod_file in mod_files:
                            method = mod_file.get('method')
                            file_path = mod_file.get('file')

                            if method == 'replace':
                                mod_file_path = os.path.join(mod_folder_path, 'mod_files', os.path.basename(file_path))
                                dest_file_path = os.path.join(modded_game_directory, file_path[1:])

                                if os.path.exists(mod_file_path):
                                    shutil.copyfile(mod_file_path, dest_file_path)
                                    print(f"File {file_path} in {mod_folder} replaced successfully.")
                                else:
                                    print(f"Mod file {file_path} in {mod_folder} not found.")

                            elif method == 'addline_bottom':
                                lines_source = mod_file.get('lines_source')
                                mod_file_path = os.path.join(mod_folder_path, 'mod_files', lines_source)
                                dest_file_path = os.path.join(modded_game_directory, file_path[1:])

                                if os.path.exists(mod_file_path):
                                    with open(mod_file_path, 'r', encoding='utf-8') as lines_file:
                                        lines_to_add = lines_file.read()

                                        with open(dest_file_path, 'a', encoding='utf-8') as dest_file:
                                            dest_file.write('\n' + lines_to_add)
                                            print(f"Lines added to {file_path} from {lines_source} successfully.")
                                else:
                                    print(f"Lines source file {lines_source} not found for {mod_folder}.")
                            
                            elif method == 'addline_top':
                                lines_source = mod_file.get('lines_source')
                                mod_file_path = os.path.join(mod_folder_path, 'mod_files', lines_source)
                                dest_file_path = os.path.join(modded_game_directory, file_path[1:])

                                if os.path.exists(mod_file_path):
                                    with open(mod_file_path, 'r', encoding='utf-8-sig') as lines_file:
                                        lines_to_add = lines_file.read().strip() + '\n'
                                        with open(dest_file_path, 'r+', encoding='utf-8-sig') as dest_file:
                                            content = dest_file.read()
                                            dest_file.seek(0, 0)
                                            dest_file.write(lines_to_add + content)
                                            print(f"Lines added to the top of {file_path} from {lines_source} successfully.")
                                else:
                                    print(f"Lines source file {lines_source} not found for {mod_folder}.")

                            elif method == 'addline_safe':
                                lines_source = mod_file.get('lines_source')
                                mod_file_path = os.path.join(mod_folder_path, 'mod_files', lines_source)
                                dest_file_path = os.path.join(modded_game_directory, file_path[1:])

                                if os.path.exists(mod_file_path):
                                    with open(mod_file_path, 'r', encoding='utf-8') as lines_file:
                                        lines_to_add = lines_file.read().strip() + '\n'

                                        with open(dest_file_path, 'r+', encoding='utf-8') as dest_file:
                                            content = dest_file.readlines()
                                            label_found = False

                                            for index, line in enumerate(content):
                                                if line.strip().startswith("label"):
                                                    content.insert(index, lines_to_add)
                                                    label_found = True
                                                    break
                                                
                                            if not label_found:
                                                print("Label not found. The code was not added.")
                                            else:
                                                dest_file.seek(0)
                                                dest_file.truncate()
                                                dest_file.write("".join(content))
                                                print(f"Lines added safely to {file_path} from {lines_source} successfully.")
                                else:
                                    print(f"Lines source file {lines_source} not found for {mod_folder}.")


                            elif method == 'replace_label':
                                file_path = mod_file.get('file')
                                old_label_name = mod_file.get('old_label_name')
                                label_source = mod_file.get('label_source')
                            
                                mod_file_path = os.path.join(mod_folder_path, 'mod_files', label_source)
                                dest_file_path = os.path.join(modded_game_directory, file_path[1:])
                            
                                if os.path.exists(mod_file_path):
                                    with open(mod_file_path, 'r', encoding='utf-8') as label_file:
                                        new_label_content = label_file.read()
                            
                                        with open(dest_file_path, 'r', encoding='utf-8') as dest_file:
                                            content = dest_file.read()
                            
                                            label_start = content.find(f"label {old_label_name}:")
                                            if label_start != -1:
                                                label_end = content.find(f"label ", label_start + len(old_label_name) + 8)
                                                if label_end == -1:
                                                    label_end = len(content)
                                                
                                                replaced_content = content[:label_start] + new_label_content + content[label_end:]
                                                
                                                with open(dest_file_path, 'w', encoding='utf-8') as dest_file_write:
                                                    dest_file_write.write(replaced_content)
                                                    print(f"Label {old_label_name} replaced successfully in {file_path} from {label_source}.")
                                            else:
                                                print(f"Label {old_label_name} not found in {file_path}.")
                                else:
                                    print(f"Label source file {label_source} not found for {mod_folder}.")
                            elif method == 'replace_line':
                                file_path = mod_file.get('file')
                                line_to_replace = mod_file.get('line')
                                replacement_line = mod_file.get('replacement_line')

                                dest_file_path = os.path.join(modded_game_directory, file_path[1:])

                                if os.path.exists(dest_file_path):
                                    with open(dest_file_path, 'r', encoding='utf-8') as dest_file:
                                        content = dest_file.readlines()

                                        line_found = False
                                        for index, line in enumerate(content):
                                            if line.strip() == line_to_replace:
                                                content[index] = replacement_line + '\n'

                                                with open(dest_file_path, 'w', encoding='utf-8') as dest_file_write:
                                                    dest_file_write.write(''.join(content))
                                                    print(f"Line replaced successfully in {file_path}.")
                                                line_found = True
                                                break
                                            
                                        if not line_found:
                                            print(f"Line '{line_to_replace}' not found in {file_path}.")
                                else:
                                    print(f"File {file_path} not found.")

                except json.JSONDecodeError as e:
                    print(f"Error decoding autoapply.tkml in {mod_folder}: {e}")
        else:
            print(f"No autoapply.tkml found in {mod_folder} or it's not a valid mod folder.")
    waitfunc()
    waitfunc()

def clear_log_file():
    log_path = os.path.join("modded_game", "log.txt")
    if os.path.exists(log_path):
        try:
            os.remove(log_path)
            with open(log_path, 'w'):
                pass
            print("Log file cleared.")
        except Exception as e:
            print(f"Error clearing log file: {e}")
    else:
        print("Log file not found.")

def wait_for_timekeeper():
    attempts = 0

    while True:
        try:
            output = subprocess.check_output(["tasklist", "/FI", "IMAGENAME eq Timekeeper.exe"])
            decoded_output = output.decode("utf-8", errors="replace")
            process_started = "Timekeeper.exe" in decoded_output

            if process_started:
                print("TimeKeeper.exe process detected!")
                break
            else:
                attempts += 1
                print(f"Attempt {attempts} failed: Process not found")
        except subprocess.CalledProcessError as e:
            attempts += 1
            print(f"Attempt {attempts} failed: {e}")

        time.sleep(0.5)

def check_timekeeper():
    try:
        output = subprocess.check_output(["tasklist", "/FI", "IMAGENAME eq Timekeeper.exe"])
        decoded_output = output.decode("utf-8", errors="replace")
        process_started = "Timekeeper.exe" in decoded_output
        return process_started
    except subprocess.CalledProcessError as e:
        print(f"Error checking for Timekeeper.exe: {e}")
        return False

def live_debugger():
    log_path = os.path.join("modded_game", "log.txt")
    if os.path.exists(log_path):
        try:
            with open(log_path, 'r') as log_file:
                while check_timekeeper():
                    lines = log_file.readlines()
                    for line in lines:
                        print(line, end='')

                    time.sleep(0.1)
        except Exception as e:
            print(f"Error reading log file: {e}")
    else:
        print("Log file not found.")

def print_center(text):
    terminal_width = os.get_terminal_size().columns
    lines = text.split('\n')
    for line in lines:
        print(line.center(terminal_width))

ver = "0.0.2"  # Update the version number

init()

ascii_art = (
    " ▀▀█▀▀ ▀  █▀▄▀█ █▀▀  █    ▄▀▀▄ ▄▀▀▄ █▀▀▄ █▀▀ █▀▀▄ █▀█\n"
    "   █   █▀ █ ▀ █ █▀▀  █  ▄ █  █ █▄▄█ █  █ █▀▀ █▄▄▀  ▄▀\n"
    "   █  ▀▀▀ ▀   ▀ ▀▀▀  ▀▀▀▀  ▀▀  ▀  ▀ ▀▀▀  ▀▀▀ ▀ ▀▀ █▄▄"
)

while True:
    clean_start()
    clear_screen()
    print(Fore.LIGHTRED_EX)
    print_center(ascii_art)
    print(Style.RESET_ALL)
    print(Fore.YELLOW + f"Version {ver}".center(os.get_terminal_size().columns))
    print(Fore.LIGHTYELLOW_EX + "by KRWCLASSIC".center(os.get_terminal_size().columns) + Style.RESET_ALL + "\n")
    print("1) Load Base Game")
    print("2) Load Modded Game")
    print("3) Mod List")
    print("4) Build Modded Game")
    print("5) Run Modded Game in Debug Mode")
    print("6) Update and Download Time Keeper")

    option = input("   Option: ")

    if option == '1':
        load_game("basegame")
    elif option == '2':
        load_game("modded_game")
    elif option == '3':
        extract_mods()
        show_mod_list()
    elif option == '4':
        extract_mods()
        check_mod_ids()
        check_conflicting_mod_ids()
        check_mod_files()
        display_mod_info()
        create_modded_instance()
        apply_mods()
    elif option == '5':
        clear_log_file()
        load_game("modded_game")
        wait_for_timekeeper()
        live_debugger()
    elif option == '6':
        pass