### This function creates the necessary symlinks for the different functions so that when they get zipped, they take their dependencies with them.

import os,sys

if str(sys.platform).lower().startswith('win'):
    is_windows=True
else:
    is_windows=False

orig_cwd = os.getcwd()

root_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

depends_dict = {
    'dnd_dice_roller':['commons'],
    'dnd_loot_generator':['commons'],
    'dnd_harptos_calendar':[],
    'dnd_age_converter':['commons','../numpy_stash'],
    'dnd_names_generator':['commons'],
    'harambe':['commons']
    }
    
for f in depends_dict:
    for d in depends_dict[f]:
        folder_to_link = os.path.join(root_dir,'src',d)
        link_location = os.path.join(root_dir,'src',f,os.path.basename(d))
        if is_windows:
            symlink_cmd = f'mklink /D {link_location} {folder_to_link}'
        else:
            symlink_cmd = f'ln -s {folder_to_link} {link_location}'
        os.system(symlink_cmd)
