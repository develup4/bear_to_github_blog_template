cd _drafts
python3 publish.py
cd ..
today=$(date "+%Y%m%d")
git add .
git commit -m "${today}"
git push origin master