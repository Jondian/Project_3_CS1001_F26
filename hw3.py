import data
import build_data

full_data = build_data.get_data()

# PART 1: Total Population
# Function 1: find the total population of a given list of counties
def population_total(counties: list[data.CountyDemographics]) -> int:
    totalPopulation = 0
    for county in counties: # goes through the counties in the given parameter
        totalPopulation += county.population['2014 Population'] # adds the populations in each county by the 2014 population dictionary
    return totalPopulation # returns the sum of all populations in the county

# PART 2: Filter Countries by State
# Function 2: filter counties by state
def filter_by_state(counties: list[data.CountyDemographics], state: str) -> list[data.CountyDemographics]:
    countyList = [] # creates new list
    for county in counties:
        if county.state == state: # checks if county state is the same as the state filter
            countyList.append(county) # adds county to new list if it matches with the filter
    return countyList # returns new list

# PART 3: Calculate Sub-Populations
# Function 3: filter population by education
def population_by_education(counties: list[data.CountyDemographics], key: str) -> float:
    totalPopulation = 0 # accumulator for the populations that 
    for county in counties: # for loop to go through the list of counties
        totalPopulation += (county.population['2014 Population'] * (county.education.get(key,0) / 100)) # multiplies the population of the county by the percentage of people that have the given education
    return totalPopulation 

# Function 4: filter population by ethnicty
def population_by_ethnicity(counties: list[data.CountyDemographics], key: str) -> float:
    totalPopulation = 0 
    for county in counties: # for loop to go through the list of counties
        totalPopulation += (county.population['2014 Population'] * (county.ethnicities.get(key,0) / 100))# multiplies the population of the county by the percentage of people that are the given ethnicity in the parameter
    return totalPopulation 

# Function 5: filter population by people under poverty levels
def population_below_poverty_level(counties: list[data.CountyDemographics]) -> float:
    totalPopulation = 0 
    for county in counties:# for loop to go through the list of counties
        totalPopulation += (county.population['2014 Population'] * (county.income['Persons Below Poverty Level'] / 100))# multiplies the population of the county by the percentage of people that are below poverty level
    return totalPopulation 

# PART 4: Calculate Overall Percentage
# Function 6: Calculate Percent by Education
def percent_by_education(counties: list[data.CountyDemographics], key: str) -> float:
    totalCountiesPopulation = population_total(counties)
    if totalCountiesPopulation == 0:
        return 0
    subCountiesPopulation = population_by_education(counties, key)
    return 100 * (subCountiesPopulation/totalCountiesPopulation)

# Function 7: Calculate Percent by Ethnicity
def percent_by_ethnicity(counties: list[data.CountyDemographics], key: str) -> float:
    totalCountiesPopulation = population_total(counties)
    if totalCountiesPopulation == 0:
        return 0
    subCountiesPopulation = population_by_ethnicity(counties, key)
    return 100 * (subCountiesPopulation/totalCountiesPopulation)
# Function 8: Calculate Percent by Poverty
def percent_below_poverty_level(counties: list[data.CountyDemographics]) -> float:
    totalCountiesPopulation = population_total(counties)
    if totalCountiesPopulation == 0:
        return 0
    subCountiesPopulation = population_below_poverty_level(counties)
    return 100 * (subCountiesPopulation/totalCountiesPopulation)

def thingy(thing: list[int]) -> int:
    default = -1
    for i in range(len(thing)):
        if thing[i] == 4:
            return i
    return default
print(thingy([1,2,3,1,2,5]))
# PART 5: Filter Counties by Demographic Thresholds
# Function 9
