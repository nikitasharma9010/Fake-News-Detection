from imports import pd
from global_variables import TRUE_NEWS_FILE
from global_variables import FAKE_NEWS_FILE

# load files
true = pd.read_csv(TRUE_NEWS_FILE)
fake = pd.read_csv(FAKE_NEWS_FILE)