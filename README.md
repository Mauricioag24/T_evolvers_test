## T_Evolvers_Test
# Rest Api
In the first numeral of this test, it was requested to perform a rest api where a reservation api is created, for it's operation the following procedure must be carried out:
1. If you are using Windows Download WSL with Ubuntu and install docker or Docker Desktop and Docker-compose
2. Enter in the path where you cloned the repository and enter in the Rest Api folder
3. In Ubuntu distro with WSL or in PowerShell if you use Docker Desktop, please run the command: docker-compose up -d and wait until the Database installation Finish. In this project i use Elasticsearch with kibana as Database.
4. When the database installation finish please check that the cointener is running in the URL: Localhost:9200
5. If the Locahost is runinng, now you can run the main.py in VSCODE or in the Ubuntu terminal with the command: python3 main.py

Note: In Docker Desktop before run docker-compose file please enter the following commands:
- wsl -d docker-desktop 
- sysctl -w vm.max_map_count=262144

Please in python install flask and elasticsearch with commands:
- pip install elasticsearch
- pip install flask

#Web Scrapp
In the second numeral of the test, it was requested to perform a web scrapp in the webpage "". The function of this web scrapp is to select two items of each category and add to cart. To execute this script you need to follow the following steps:
1. Open PowerShell terminal in Windows
2. In the terminal go to the project path and enter in WebScrapp folder
3. Run the script in VSCODE or in PowerShell terminal with the command: python models.py
