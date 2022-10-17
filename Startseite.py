import streamlit as st
import pickle
import random
import streamlit_authenticator as stauth
import string
import seiten.kampagnenbericht_gesamt as kampagnenbericht_gesamt
import seiten.kampagnenbericht_google_ads as kampagnenbericht_google_ads
import seiten.kampagnenbericht_keywords as kampagnenbericht_keywords
import seiten.kampagnenbericht_microsoft_ads as kampagnenbericht_microsoft_ads

st.set_page_config(
    page_title="PONE Standardreporting",
    page_icon="📋",
)

st.title("Startseite PONE Standardreporting")


# with open('auth/credentials.pkl', 'rb') as f:
#     loaded_dict = pickle.load(f)
    

# def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))

# random_key = id_generator()
# #name, username, pw, cookiename in browser, randomkey to hash cookie signature, number of days the cookie can used for, 0 now expiraton
# authenticator = stauth.Authenticate(loaded_dict, "drg_dashboard", random_key, cookie_expiry_days = 1)

# name, authenticaton_status, username = authenticator.login("Login", "main")

# if  authenticaton_status == False:
#     st.error("Username/password is incorrect")
     
# if  authenticaton_status == None:
#     st.warning("Please enter your username and password")
    
# if  authenticaton_status:
#     if loaded_dict['usernames'][f'{username}']['role'] == 'ADMIN':
#         tabs = st.tabs(['Kampagnenbericht Gesamt', 'Kampagnenbericht Google Ads', 'Kampagnenbericht Microsoft Ads', 'Kampagnenbericht Keywords', 'Admin'])
        
#         with tabs[0]:
#             kampagnenbericht_gesamt.run_kampagnenbericht()
#         with tabs[1]:
#             kampagnenbericht_google_ads.run_kampagnenbericht()
#         with tabs[2]:
#             kampagnenbericht_microsoft_ads.run_kampagnenbericht()
#         with tabs[3]:
#             kampagnenbericht_keywords.run_kampagnenbericht()
#         with tabs[4]:
#             st.title('Admin')
#             st.text("Hier wird noch eine Adminseite erstellt...")
#     else:        
#     # if loaded_dict['usernames'][f'{username}']['role'] == 'VIEWER':
#         tabs = st.tabs(['Kampagnenbericht Gesamt', 'Kampagnenbericht Google Ads', 'Kampagnenbericht Microsoft Ads', 'Kampagnenbericht Keywords'])
        
#         with tabs[0]:
#             kampagnenbericht_gesamt.run_kampagnenbericht()
#         with tabs[1]:
#             kampagnenbericht_google_ads.run_kampagnenbericht()
#         with tabs[2]:
#             kampagnenbericht_microsoft_ads.run_kampagnenbericht()
#         with tabs[3]:
#             kampagnenbericht_keywords.run_kampagnenbericht()
     

#     # ---- SIDEBAR ----
#     st.sidebar.title(f"Welcome *{name}*!")
#     # st.sidebar.header("Please Filter Here:")
#     with st.sidebar:
#         authenticator.logout("Logout", "main")

tabs = st.tabs(['Kampagnenbericht Gesamt', 'Kampagnenbericht Google Ads', 'Kampagnenbericht Microsoft Ads', 'Kampagnenbericht Keywords', 'Admin'])
        
with tabs[0]:
    kampagnenbericht_gesamt.run_kampagnenbericht()
with tabs[1]:
    kampagnenbericht_google_ads.run_kampagnenbericht()
with tabs[2]:
    kampagnenbericht_microsoft_ads.run_kampagnenbericht()
with tabs[3]:
    kampagnenbericht_keywords.run_kampagnenbericht()
with tabs[4]:
    st.title('Admin')
    st.text("Hier wird noch eine Adminseite erstellt...")