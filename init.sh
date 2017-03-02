# init.sh
# reinitializes dev environment

RED='\033[0;31m'
NC='\033[0m' # No Color

printf "${RED}rebuilding python dev environment @ venv...${NC}\n"
rm -r venv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt