
### **📄 cod (`population.py`)**  
```python
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population"

def get_population():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", {"class": "wikitable"})
    states_data = {}

    for row in table.find_all("tr")[1:]:  # Skip header row
        cols = row.find_all("td")
        if cols:
            state = cols[1].text.strip()
            population = cols[2].text.strip().replace(",", "")
            states_data[state] = population

    return states_data

if __name__ == "__main__":
    states_population = get_population()
    state_name = input("Enter state name: ")
    print(f"Population of {state_name}: {states_population.get(state_name, 'Not found')}")
