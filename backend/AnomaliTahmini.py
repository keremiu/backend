
import pandas as pd
import json

from myDB import myDB


misli_data = myDB.get_data_from_mongo('BahisSiteleriCur2', 'misli')
nesine_data = myDB.get_data_from_mongo('BahisSiteleriCur2', 'nesine')
bet10_data = myDB.get_data_from_mongo('BahisSiteleriCur2', 'bet10')
sport888_data = myDB.get_data_from_mongo('BahisSiteleriCur2', '888sport')
betway_data = myDB.get_data_from_mongo('BahisSiteleriCur2', 'betway')
unibet_data = myDB.get_data_from_mongo('BahisSiteleriCur2', 'unibet')
marathon_data = myDB.get_data_from_mongo('BahisSiteleriCur2', 'marathon')
tuttur_data = myDB.get_data_from_mongo('BahisSiteleriCur2', 'tuttur')

'''with open('misli.json') as file:
    misli_data = json.load(file)
with open('nesine.json') as file:
    nesine_data = json.load(file)
with open('10bet.json') as file:
    bet10_data = json.load(file) 
with open('888sport.json') as file:
    sport888_data = json.load(file)
with open('betway.json') as file:
    betway_data = json.load(file)
with open('unibet.json') as file:
    unibet_data = json.load(file)
with open('marathon.json') as file:
    marathon_data = json.load(file) 
with open('tuttur.json') as file:
    tuttur_data = json.load(file)'''


df_nesine = pd.DataFrame(nesine_data)
df_bet10 = pd.DataFrame(bet10_data)
df_sport888 = pd.DataFrame(sport888_data)
df_misli = pd.DataFrame(misli_data)
df_betway = pd.DataFrame(betway_data)
df_unibet = pd.DataFrame(unibet_data)
df_marathon = pd.DataFrame(marathon_data)
df_tuttur = pd.DataFrame(tuttur_data)

# Convert 'Teams' and '1x2' columns from dict to list and create new dataframes
df_misli_teams = pd.DataFrame([(k,v) for d in df_misli['Teams'] for k,v in d.items()], columns=['index','Teams'])
df_misli_1x2 = pd.DataFrame([(k,v) for d in df_misli['1x2'] for k,v in d.items()], columns=['index','1x2'])

df_marathon_teams = pd.DataFrame([(k,v) for d in df_marathon['Teams'] for k,v in d.items()], columns=['index','Teams'])
df_marathon_1x2 = pd.DataFrame([(k,v) for d in df_marathon['1x2'] for k,v in d.items()], columns=['index','1x2'])

df_bet10_teams = pd.DataFrame([(k,v) for d in df_bet10['Teams'] for k,v in d.items()], columns=['index','Teams'])
df_bet10_1x2 = pd.DataFrame([(k,v) for d in df_bet10['1x2'] for k,v in d.items()], columns=['index','1x2'])

df_nesine_teams = pd.DataFrame([(k,v) for d in df_nesine['Teams'] for k,v in d.items()], columns=['index','Teams'])
df_nesine_1x2 = pd.DataFrame([(k,v) for d in df_nesine['1x2'] for k,v in d.items()], columns=['index','1x2'])

df_tuttur_teams = pd.DataFrame([(k,v) for d in df_tuttur['Teams'] for k,v in d.items()], columns=['index','Teams'])
df_tuttur_1x2 = pd.DataFrame([(k,v) for d in df_tuttur['1x2'] for k,v in d.items()], columns=['index','1x2'])

df_sport888_teams = pd.DataFrame([(k,v) for d in df_sport888['Teams'] for k,v in d.items()], columns=['index','Teams'])
df_sport888_1x2 = pd.DataFrame([(k,v) for d in df_sport888['1x2'] for k,v in d.items()], columns=['index','1x2'])

df_betway_teams = pd.DataFrame([(k,v) for d in df_betway['Teams'] for k,v in d.items()], columns=['index','Teams'])
df_betway_1x2 = pd.DataFrame([(k,v) for d in df_betway['1x2'] for k,v in d.items()], columns=['index','1x2'])

df_unibet_teams = pd.DataFrame([(k,v) for d in df_unibet['Teams'] for k,v in d.items()], columns=['index','Teams'])
df_unibet_1x2 = pd.DataFrame([(k,v) for d in df_unibet['1x2'] for k,v in d.items()], columns=['index','1x2'])

# Convert 'index' column to int for proper merging
df_misli_teams['index'] = df_misli_teams['index'].astype(int)
df_misli_1x2['index'] = df_misli_1x2['index'].astype(int)

df_marathon_teams['index'] = df_marathon_teams['index'].astype(int)
df_marathon_1x2['index'] = df_marathon_1x2['index'].astype(int)

df_bet10_teams['index'] = df_bet10_teams['index'].astype(int)
df_bet10_1x2['index'] = df_bet10_1x2['index'].astype(int)

df_nesine_teams['index'] = df_nesine_teams['index'].astype(int)
df_nesine_1x2['index'] = df_nesine_1x2['index'].astype(int)

df_tuttur_teams['index'] = df_tuttur_teams['index'].astype(int)
df_tuttur_1x2['index'] = df_tuttur_1x2['index'].astype(int)

df_sport888_teams['index'] = df_sport888_teams['index'].astype(int)
df_sport888_1x2['index'] = df_sport888_1x2['index'].astype(int)

df_betway_teams['index'] = df_betway_teams['index'].astype(int)
df_betway_1x2['index'] = df_betway_1x2['index'].astype(int)

df_unibet_teams['index'] = df_unibet_teams['index'].astype(int)
df_unibet_1x2['index'] = df_unibet_1x2['index'].astype(int)

# Merge the two dataframes on 'index'
df_misli = pd.merge(df_misli_teams, df_misli_1x2, on='index')
df_marathon = pd.merge(df_marathon_teams, df_marathon_1x2, on='index')
df_bet10 = pd.merge(df_bet10_teams, df_bet10_1x2, on='index')
df_nesine = pd.merge(df_nesine_teams, df_nesine_1x2, on='index')
df_tuttur = pd.merge(df_tuttur_teams, df_tuttur_1x2, on='index')
df_sport888 = pd.merge(df_sport888_teams, df_sport888_1x2, on='index')
df_betway = pd.merge(df_betway_teams, df_betway_1x2, on='index')
df_unibet = pd.merge(df_unibet_teams, df_misli_1x2, on='index')


df_marathon['teams_normalized'] = df_marathon['Teams'].str.lower().str.replace(' ', '')
df_bet10['teams_normalized'] = df_bet10['Teams'].str.lower().str.replace(' ', '')
df_misli['teams_normalized'] = df_misli['Teams'].str.lower().str.replace(' ', '')
df_nesine['teams_normalized'] = df_nesine['Teams'].str.lower().str.replace(' ', '')
df_tuttur['teams_normalized'] = df_tuttur['Teams'].str.lower().str.replace(' ', '')
df_sport888['teams_normalized'] = df_sport888['Teams'].str.lower().str.replace(' ', '')
df_betway['teams_normalized'] = df_betway['Teams'].str.lower().str.replace(' ', '')
df_unibet['teams_normalized'] = df_unibet['Teams'].str.lower().str.replace(' ', '')


def normalize_team_name(name):
    name = name.lower().strip()
    name = name.replace("a.ş.", "").strip()  
    name = name.replace("sk", "").strip()  
    name = name.replace("fk", "").strip() 
    name = name.replace("jk", "").strip() 
    name = name.replace("mke", "").strip() 
    name = name.replace("ç", "c")
    name = name.replace("ş", "s")
    name = name.replace("ğ", "g")
    name = name.replace("ü", "u")
    name = name.replace("ö", "o")
    name = name.replace("ı", "i")
    name = name.replace("fatih karagumruk", "fatihkaragumruk").strip()
    name = name.replace("f.karagümruk", "fatihkaragumruk").strip()  
    name = name.replace("fatihkaragumrukistanbul", "fatihkaragumruk").strip()  
    name = name.replace("adana demir", "adana demirspor").strip()  
    return name


df_misli['teams_normalized'] = df_misli['teams_normalized'].apply(normalize_team_name)
df_nesine['teams_normalized'] = df_nesine['teams_normalized'].apply(normalize_team_name)
df_sport888['teams_normalized'] = df_sport888['teams_normalized'].apply(normalize_team_name)
df_betway['teams_normalized'] = df_betway['teams_normalized'].apply(normalize_team_name)
df_unibet['teams_normalized'] = df_unibet['teams_normalized'].apply(normalize_team_name)
df_bet10['teams_normalized'] = df_bet10['teams_normalized'].apply(normalize_team_name)
df_marathon['teams_normalized'] = df_marathon['teams_normalized'].apply(normalize_team_name)
df_tuttur['teams_normalized'] = df_tuttur['teams_normalized'].apply(normalize_team_name)


# In[11]:


df_misli_sorted = df_misli.sort_values('teams_normalized').reset_index(drop=True)
df_nesine_sorted = df_nesine.sort_values('teams_normalized').reset_index(drop=True)
df_sport888_sorted = df_sport888.sort_values('teams_normalized').reset_index(drop=True)
df_betway_sorted = df_betway.sort_values('teams_normalized').reset_index(drop=True)
df_unibet_sorted = df_unibet.sort_values('teams_normalized').reset_index(drop=True)
df_bet10_sorted = df_bet10.sort_values('teams_normalized').reset_index(drop=True)
df_marathon_sorted = df_marathon.sort_values('teams_normalized').reset_index(drop=True)
df_tuttur_sorted = df_tuttur.sort_values('teams_normalized').reset_index(drop=True)


import numpy as np


result_misli = df_misli_sorted['1x2'].tolist()
result_nesine = df_nesine_sorted['1x2'].tolist()
result_sport888 = df_sport888_sorted['1x2'].tolist()
result_betway = df_betway_sorted['1x2'].tolist()
result_unibet = df_unibet_sorted['1x2'].tolist()
result_bet10 = df_bet10_sorted['1x2'].tolist()
result_marathon = df_marathon_sorted['1x2'].tolist()
result_tuttur = df_tuttur_sorted['1x2'].tolist()


from AnomalyDetector import AnomalyDetector


import numpy as np

def find_max_elements_and_anomalies(*matrices, matrix_names, threshold=1.4):
    if len(matrices) != len(matrix_names):
        raise ValueError("Number of matrices and matrix names must be equal")

    rows = len(matrices[0])
    cols = len(matrices[0][0])

    # Check all matrices have the same dimensions
    for matrix in matrices:
        if len(matrix) != rows or len(matrix[0]) != cols:
            raise ValueError("All matrices must have the same dimensions")

    max_matrix = [[None] * cols for _ in range(rows)]
    anomaly_matrix = [[None] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            max_element = float('-inf')
            max_name = None
            anomalies = []
            elements = []
            for matrix, name in zip(matrices, matrix_names):
                element = float(matrix[i][j])
                elements.append(element)
                if element > max_element:
                    max_element = element
                    max_name = name
            anomaly_detector = AnomalyDetector(threshold)
            anomaly_detector.fit(np.array(elements))
            if anomaly_detector.detect_anomalies(np.array(elements)).any():
                anomalies = [name for idx, name in enumerate(matrix_names) if anomaly_detector.detect_anomalies(np.array(elements))[idx]]

            max_matrix[i][j] = max_name
            anomaly_matrix[i][j] = anomalies if anomalies else None

    return max_matrix, anomaly_matrix
max_matrix, anomaly_matrix = find_max_elements_and_anomalies(result_misli, result_nesine, result_sport888,result_betway,result_unibet,result_bet10,result_marathon,result_tuttur, matrix_names=["misli", "nesine", "888sport", "betway", "unibet","bet10","marathon","tuttur"], threshold=1.7)


'''dict_misli = {'Teams': df_misli_sorted['Teams'], '1x2': df_misli_sorted['1x2'], 'teams_normalized': df_misli_sorted['teams_normalized']}
dict_nesine = {'Teams': df_nesine_sorted['Teams'], '1x2': df_nesine_sorted['1x2'], 'teams_normalized': df_nesine_sorted['teams_normalized']}
dict_sport888 = {'Teams': df_sport888_sorted['Teams'], '1x2': df_sport888_sorted['1x2'], 'teams_normalized': df_sport888_sorted['teams_normalized']}
dict_betway = {'Teams': df_betway_sorted['Teams'], '1x2': df_betway_sorted['1x2'], 'teams_normalized': df_betway_sorted['teams_normalized']}
dict_unibet = {'Teams': df_unibet_sorted['Teams'], '1x2': df_unibet_sorted['1x2'], 'teams_normalized': df_unibet_sorted['teams_normalized']}
dict_bet10 = {'Teams': df_bet10_sorted['Teams'], '1x2': df_bet10_sorted['1x2'], 'teams_normalized': df_bet10_sorted['teams_normalized']}
dict_marathon = {'Teams': df_marathon_sorted['Teams'], '1x2': df_marathon_sorted['1x2'], 'teams_normalized': df_marathon_sorted['teams_normalized']}
dict_tuttur = {'Teams': df_tuttur_sorted['Teams'], '1x2': df_tuttur_sorted['1x2'], 'teams_normalized': df_tuttur_sorted['teams_normalized']}


# Convert the lists to DataFrames
df_mislij =  pd.DataFrame.from_dict(dict_misli)
df_nesinej =  pd.DataFrame.from_dict(dict_nesine)
df_sport888j =  pd.DataFrame.from_dict(dict_sport888)
df_betwayj =  pd.DataFrame.from_dict(dict_betway)
df_unibetj =  pd.DataFrame.from_dict(dict_unibet)
df_bet10j =  pd.DataFrame.from_dict(dict_bet10)
df_marathonj =  pd.DataFrame.from_dict(dict_marathon)
df_tuttur =  pd.DataFrame.from_dict(dict_tuttur)

# Save DataFrames as JSON
df_mislij.to_json('misli.json')
df_nesinej.to_json('nesine.json')
df_sport888j.to_json('888sport.json')
df_betwayj.to_json('betway.json')
df_unibetj.to_json('unibet.json')
df_bet10j.to_json('bet10.json')
df_marathonj.to_json('marathon.json')
df_tuttur.to_json('tuttur.json')
if not df_mislij.empty:
    myDB.update_to_mongo('BahisSiteleriCur2', 'misli', df_mislij)

if not df_nesinej.empty:
    myDB.update_to_mongo('BahisSiteleriCur2', 'nesine', df_nesinej)

if not df_sport888j.empty:
    myDB.update_to_mongo('BahisSiteleriCur2', '888sport', df_sport888j)

if not df_betwayj.empty:
    myDB.update_to_mongo('BahisSiteleriCur2', 'betway', df_betwayj)

if not df_unibetj.empty:
    myDB.update_to_mongo('BahisSiteleriCur2', 'unibet', df_unibetj)

if not df_bet10j.empty:
    myDB.update_to_mongo('BahisSiteleriCur2', 'bet10', df_bet10j)

if not df_marathonj.empty:
    myDB.update_to_mongo('BahisSiteleriCur2', 'marathon', df_marathonj)

if not df_tuttur.empty:
    myDB.update_to_mongo('BahisSiteleriCur2', 'tuttur', df_tuttur)
#db = myDB()
#db.insert_to_mongo_from_directory('BahisSiteleriCur2', '.', files=['misli', 'nesine', '888sport', 'betway', 'unibet','bet10','marathon','tuttur'])'''


