import subprocess
import requests
import shutil
import time
import json
import sys
import os
from colorama import init, Fore, Style

def waitfunc():
    time.sleep(1)

def press_enter_to_continue():
    input("\nPress Enter to continue...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clean_start():
    for directory_name in ["temp_mods", "temp"]:
        try:
            shutil.rmtree(directory_name, ignore_errors=True)
        except Exception:
            pass

def load_game(game_path):
    clear_screen()
    
    if game_path == "modded_game":
        if check_modded_game_folder():
            print("Modded game found. Starting the game...")
            os.system(f"start {game_path.lower()}\\TimeKeeper.exe")

        else:
            print("Modded game not found. Please run and build modded game first.")
    else:
        print(f"Starting the {game_path}...")
        os.system(f"start {game_path.lower()}\\TimeKeeper.exe")


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
    modded_game_directory = os.path.normpath(modded_game_directory)

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

                            elif method == 'rename':
                                target_prepath = mod_file.get('target')
                                target = os.path.normpath(os.path.join(modded_game_directory, target_prepath[1:]))
                                new_name = mod_file.get('new_name')

                                reversed_target = target[::-1]
                                index_of_first_slash = reversed_target.find(os.sep)
                                if index_of_first_slash != -1:
                                    nametarget_reversed = reversed_target[index_of_first_slash:]
                                else:
                                    nametarget_reversed = reversed_target
                                nametarget = nametarget_reversed[::-1]

                                if os.path.exists(target):
                                    os.rename(target, os.path.join(nametarget, new_name))
                                    print(f"File or folder {target_prepath} renamed to {new_name} successfully.")
                                else:
                                    print(f"Mod file or folder {target} not found.")

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
        output = subprocess.check_output(["tasklist", "/FI", "IMAGENAME eq /C Timekeeper.exe"])
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

def download_game():
    try:
        clear_screen()
        print("Fetching the download link from the text file...")

        url = "https://raw.githubusercontent.com/KRWCLASSIC/Time-Keeper-Archive/main/newest_release.txt"
        response = requests.get(url)

        if response.status_code == 200:
            content = response.text

            # Assuming the content is a valid URL
            game_url = content.strip()

            # Create the temp folder if it doesn't exist
            temp_folder = "temp"
            if not os.path.exists(temp_folder):
                os.makedirs(temp_folder)

            clear_screen()
            print("Downloading the game...")

            # Download the game to the temp folder
            game_response = requests.get(game_url)
            if game_response.status_code == 200:
                game_path = os.path.normcase(os.path.join(temp_folder, "TimeKeeper.zip"))
                with open(game_path, "wb") as game_file:
                    game_file.write(game_response.content)
                clear_screen()
                print(f"Game downloaded successfully to '{game_path}'.")
            else:
                clear_screen()
                print(f"Failed to download the game. Status code: {game_response.status_code}")
        else:
            print(f"Failed to fetch the URL. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        waitfunc()

def extract_game():
    try:
        clear_screen()
        temp_folder = "temp"

        # Check if the temp folder exists
        if not os.path.exists(temp_folder):
            print("Temp folder not found.")
            waitfunc()
            return

        # List all game ZIP files in the temp folder
        game_zips = [f for f in os.listdir(temp_folder) if f.endswith('.zip')]
        
        if not game_zips:
            print("No game ZIP files found in the temp folder.")
            waitfunc()
            return

        # Assuming there's only one game ZIP file, you may need to handle multiple ZIP files differently
        game_zip = os.path.join(temp_folder, game_zips[0])

        print(f"Extracting {game_zip} and entering the folder...")

        # Extract the game using 7z.exe
        subprocess.run(['utils\\7z', 'x', f'-o{temp_folder}', game_zip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # List all folders in the temp folder
        folders = [f for f in os.listdir(temp_folder) if os.path.isdir(os.path.join(temp_folder, f))]
        
        if len(folders) != 1:
            raise ValueError("Expected one folder, but found multiple or none.")

        # Enter the extracted folder
        extracted_folder = os.path.join(temp_folder, folders[0])
        os.chdir(extracted_folder)

        # If all operations succeeded, call finish_download
        finish_download()

    except Exception as e:
        print(f"An error occurred: {e}")

        # Remove the temp folder recursively
        shutil.rmtree(temp_folder, ignore_errors=True)

    finally:
        waitfunc()
        clear_screen()

def finish_download():
    try:
        script_folder = os.path.dirname(os.path.abspath(__file__))
        basegame_folder = os.path.join(script_folder, "basegame")
        temp_folder = os.path.join(script_folder, "temp")

        # Remove existing basegame folder if it exists
        if os.path.exists(basegame_folder):
            shutil.rmtree(basegame_folder)

        # Ensure the basegame folder exists
        os.makedirs(basegame_folder)

        print("Moving game files to basegame folder...")

        # List all folders in the temp folder
        folders = [f for f in os.listdir(temp_folder) if os.path.isdir(os.path.join(temp_folder, f))]

        if len(folders) == 1:
            game_folder = os.path.join(temp_folder, folders[0])

            # Move all files and subfolders from the game folder to the new basegame folder
            for item in os.listdir(game_folder):
                item_path = os.path.join(game_folder, item)
                destination_path = os.path.join(basegame_folder, item)

                if os.path.isfile(item_path):
                    shutil.move(item_path, destination_path)
                elif os.path.isdir(item_path):
                    shutil.move(item_path, destination_path)

            print("Game files and folders moved successfully.")
        elif len(folders) > 1:
            raise ValueError("Expected one folder, but found multiple.")
        else:
            print("No folders found in the temp directory.")

    except Exception as e:
        print(f"An error occurred during the move operation: {e}")

    finally:
        # Change working directory to the script's directory
        os.chdir(script_folder)
        waitfunc()

def print_center(text):
    terminal_width = os.get_terminal_size().columns
    lines = text.split('\n')
    for line in lines:
        print(line.center(terminal_width))

ver = "0.0.3"  # Update the version number

init()
clean_start()

ascii_art = (
    " ▀▀█▀▀ ▀  █▀▄▀█ █▀▀  █    ▄▀▀▄ ▄▀▀▄ █▀▀▄ █▀▀ █▀▀▄ █▀█\n"
    "   █   █▀ █ ▀ █ █▀▀  █  ▄ █  █ █▄▄█ █  █ █▀▀ █▄▄▀  ▄▀\n"
    "   █  ▀▀▀ ▀   ▀ ▀▀▀  ▀▀▀▀  ▀▀  ▀  ▀ ▀▀▀  ▀▀▀ ▀ ▀▀ █▄▄"
)

while True:
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
        download_game()
        extract_game()