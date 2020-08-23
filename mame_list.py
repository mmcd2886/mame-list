#Script that will move rom files based on exported MAME list in order to create All Killer No Filler list.

import shutil
import re
import time
import traceback

#User input and directions
def main():
    export_list=input("Drag the exported MAME list here and hit Return Key: ").rstrip() 
    formatted_list=input("Drag an empty .txt file here and hit Return Key: ").rstrip() 
    rom_folder=input("Drag the folder where roms are stored here and hit Return Key: ").rstrip() + ("/")
    destination_folder=input("Drag the folder where roms will be copied to here and hit Enter Key: ").rstrip() + ("/")
    with open(export_list, 'r') as text_file_1, open(formatted_list, 'a') as text_file_2:
#remove the quotations from the list
        for line in text_file_1:
            remove_quotes = re.sub(r'".*?"', '', line)
            text_file_2.write(remove_quotes.rstrip() + '.zip' + '\n')
    time.sleep(3) 
#open the newly created text file with rom names that lists roms with .zip file extension.   
    file_not_found_errors=[]
    with open(formatted_list, 'r') as text_file_1:     
        for rom in text_file_1: 
            source = rom_folder + rom.rstrip()
            destination = destination_folder + rom.rstrip()         

            try:
                shutil.copy(source, destination)
            except FileNotFoundError as not_found:
#adds FileNoteFoundErrors to the file_not_found_errors list so they can be printed at the end
                file_not_found_errors.append(not_found.filename)
                traceback.print_exc()
                pass
        print("\n", "\n", "--------------------FILES NOT FOUND------------------------")
        for error in file_not_found_errors:
            print ("File Not Found: ", error)          
main()
