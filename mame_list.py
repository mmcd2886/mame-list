#Script that will move rom files based on exported MAME list in order to create All Killer No Filler list.

#import shutil to move files
import shutil
#import regular expression to remove quoted text in MAME exported txt
import re
#import time to activate sleep while file is created
import time
#import traceback for error reporting
import traceback

def main():
#the exported MAME list file path will be input here.
    export_list=input("Drag the exported MAME list here and hit Return Key: ").rstrip() 
#drag an empty .txt file here 
    formatted_list=input("Drag an empty .txt file here and hit Return Key: ").rstrip() 
#enter filepath to folder where roms are located
    rom_folder=input("Drag the folder where roms are stored here and hit Return Key: ").rstrip() + ("/")
#enter filepath to folder where you want roms moved
    destination_folder=input("Drag the folder where roms will be copied to here and hit Enter Key: ").rstrip() + ("/")
   #opens text file for reading, and creates text file for writing.
    with open(export_list, 'r') as text_file_1, open(formatted_list, 'a') as text_file_2:
#create a for loop to go over every line in text_file_1 (text_file_1 = the exported MAME list).
        for line in text_file_1:
#create remove_quotes variable. re.sub will use regular expression(imported at the tops re) to remove
#quotes and all text in between quotes.
            remove_quotes = re.sub(r'".*?"', '', line)
#write rom names without quotes to text_file_2. .zip will be appended to each line.
            text_file_2.write(remove_quotes.rstrip() + '.zip' + '\n')
#have the script sleep for 5 seconds to ensure text file is created before it is read
    time.sleep(3) 
#open the newly created text file with rom names that lists roms with .zip file extension.   
    file_not_found_errors=[]
    with open(formatted_list, 'r') as text_file_1:
#itereate over every line in the text file        
        for rom in text_file_1: 
#source is a variable that will have the filepath of the rom folder with the rom name
            source = rom_folder + rom.rstrip()
#destionation will have filepath of folder and rom of where roms will be copied to.
#Note:you must have the complete file path for the rom at the destination folder.
            destination = destination_folder + rom.rstrip()         

#exept FileNotFoundError will print if a file was not found 
#traceback.print_exc() is so that you can see all traceback errors. 
#Try except- rather than stop if a file is not found it will keep going .
            try:
#shutil.copy will copy the file from the source folder to the destination. 
                shutil.copy(source, destination)
            except FileNotFoundError as not_found:
#adds FileNoteFoundErrors to the file_not_found_errors list so they can be printed at the end
                file_not_found_errors.append(not_found.filename)
#traceback.print_exc() is so that you can see all traceback errors. 
                traceback.print_exc()
                pass
#header for FileNotFoundError section
        print("\n", "\n", "--------------------FILES NOT FOUND------------------------")
#iterate over file_not_found_errors list to print
        for error in file_not_found_errors:
            print ("File Not Found: ", error)
#call main function            
main()
