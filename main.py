from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def get_teams(driver):
    teams_elements = driver.find_elements(By.CLASS_NAME, 'borderRightContent')
    teams = [team.text for team in teams_elements]

    return teams

def get_goals_scored(driver):
    goals_scored_elements = driver.find_elements(By.CLASS_NAME, "gf")
    goals_scored = [goal.text for goal in goals_scored_elements if goal.text.isdigit()]

    return goals_scored

def get_goals_conceded(driver):
    goals_conceded_elements = driver.find_elements(By.CLASS_NAME, "ga")
    goals_conceded = [goal.text for goal in goals_conceded_elements if goal.text.isdigit()]

    return goals_conceded

url = "https://footystats.org/pt/england/premier-league"

driver = webdriver.Chrome()
driver.get(url)

teams = get_teams(driver)
goals_scored = get_goals_scored(driver)
goals_conceded = get_goals_conceded(driver)

driver.quit()

data = {
    "Equipes": teams,
    "Gols marcados": goals_scored,
    "Gols sofridos": goals_conceded
}
df = pd.DataFrame(data)

filename = "Estatisticas Premier League.xlsx"
df.to_excel(filename, index=False)