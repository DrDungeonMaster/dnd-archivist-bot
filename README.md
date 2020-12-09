# dnd-archivist-bot
A collection of D&D-related functions designed to be used in Slack and powered by AWS Lambda.

December 8th, 2020: 
Added basic setup scripts. Before trying to run any of the code in this repo, you should run 'python symlink_dependencies.py'.
This will create the necessary symlinks to dependencies so that all the functions will work.
Afterwards, if you intend to upload code to AWS Lambda functions, you can run 'python zip_functions.py' to create zip archives for upload.

Also adds images. The dice-roller outputs have special effects for d20 rolls of 1 and 20. 
You should upload, at the very least, the nat-20 and crit-fail GIFs to your Slack workspace as emojis, using those exact names.
Any other images are those used in my own Slack workspace (may be inside-jokes) and are completely optional.

Includes the image I personally use for my 'Archivist' bot, which is the art from the Magic: The Gathering card, 'Curious Homunculus'.

December 7th, 2020: 
Initial commit. Expect very poor documentation and stability at this time.
