### This script will turn all the various function folders into .ZIP files for you, with the necessary dependencies included so you can upload them to AWS Lambda.
### If there are some you are not interested in, you can comment them out of the list below.

import os,sys

orig_cwd = os.getcwd()

root_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

functs_to_zip=[
    'dnd_dice_roller',
    'dnd_loot_generator',
    'dnd_harptos_calendar',
    'dnd_age_converter',
    'dnd_names_generator',
    'harambe'
    ]

for f in functs_to_zip:
    folder_to_zip = os.path.join(root_dir,'src',f)
    zip_out = f'../../{f}.zip'
    if os.path.isdir(folder_to_zip):
        os.chdir(folder_to_zip)
        if os.path.isdir('__pycache__'):
            os.system('rm -r __pycache__')
        if os.path.isdir('commons/__pycache__'):
            os.system('rm -r commons/__pycache__')
        if os.path.isfile(zip_out):
            os.system(f'rm {zip_out}')
        print(f'Zipping {f}...')
        zip_cmd = f'zip -r {zip_out} *'
        os.system(zip_cmd)
        os.chdir(orig_cwd)