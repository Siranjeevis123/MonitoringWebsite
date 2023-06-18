# Monitoring
git init
git add .
git commit -m "Your commit message"
git remote add origin <repository_URL>
git push -u origin master

# ERROR
siranjeevi@Siranjeevis-MBP Sys_montioring % git push -u origin master
Username for 'https://github.com': siranjeevis123
Password for 'https://siranjeevis123@github.com':

# Solution
git remote -v
git remote remove origin
git remote add origin git@github.com:Siranjeevis123/Monitoring.git
git push -u origin master

# main cmt
sudo python3 app.py
