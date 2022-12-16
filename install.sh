echo 'Installing cmdtaskmanager...'
mkdir -p ~/.config
cd ~/.config
python3 -m pip install -e git+https://github.com/obaranovskyi/cmdtaskmanager.git#egg=cmdtaskmanager
cd ~/.config/src/cmdenglishassist
pip install -r requirements.txt
echo 'cmdtaskmanager installed'
