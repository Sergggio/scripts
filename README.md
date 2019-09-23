# scripts
Useful python scripts

To run using Jenkins:

virtualenv --no-site-packages venv
source venv/bin/activate

pip install -q -U pip paramiko scp requests
or
pip install -r $WORKSPACE/script/requirements.txt --upgrade # If you want to use txt file
cd $WORKSPACE/script
python your_file.py
