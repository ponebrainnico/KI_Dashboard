import pandas as pd
import pickle
import streamlit_authenticator as stauth

#---- generate DF with first user ----
df = pd.DataFrame({
  'username':'pone',
  'name': 'pone',
  'password': stauth.Hasher(['abc123']).generate(),
  'role': 'ADMIN'})

def inser_user(df, username, name, password, role = 'ADMIN'):
    if username not in df.username:
        print("Nutzer ist noch nicht in DB. Der Nutzer wird nun hinzugefügt")
        return pd.concat([df, pd.DataFrame.from_records({'username':username, 'name':name, 'password':stauth.Hasher([password]).generate(), 'role':role})],ignore_index=True)
        
    else:
        print("Nutzer schonn in DB. Kann daher nicht hinzugefügt werden.")
 
df = inser_user(df, 'kunde1', 'kunde1', 'abc123', role = 'VIEWER')


#---- Generate credentials and save ----
credentials = {}
credentials['usernames'] = {}
credentials['cookie'] = {}
credentials['cookie']['expiry_days'] = 30
credentials['cookie']['key'] = 'aribvansdjasdgas'
credentials['cookie']['name'] = 'test_dashboard'

for user in df.username:    
    credentials['usernames'][user] = {}
    credentials['usernames'][user]['name'] = df[df.username == user].name.values[0]
    credentials['usernames'][user]['password'] = df[df.username == user].password.values[0]
    credentials['usernames'][user]['role'] = df[df.username == user].role.values[0]

with open('credentials.pkl', 'wb') as f:
    pickle.dump(credentials, f)