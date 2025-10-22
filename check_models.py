import google.generativeai as genai

genai.configure(api_key="AIzaSyD-3cUsmxxGwhOfFsOSnugWKdghKPR2GGw")

for m in genai.list_models():
     print(m.name)