import pandas as pd
from collections import Counter   #Counter(["good","bad","good"]) --->{'good':2,'bad':1}
import re 

# ------- Keyword Cleaning ----------
def extract_keywords(text):
    text=str(text).lower() 
    text=re.sub(f"[^a-z\s]","",text)
    words=text.split()
    return words

#----- Main Execution -------
if __name__=="__main__":
    
    # input from milestone 2
    df=pd.read_csv("Milestone2_Seniment_Results.csv")

    #--extrract keywords from clean feedback
    all_words=[]
    df["clean_feedback"].apply(lambda x: all_words.extend(extract_keywords(x)))

    #Count keywords frequencies
    keywords_freq=Counter(all_words)
    
    # Convert to Dataframe
    keywords_df=pd.DataFrame(keywords_freq.items(),columns=["keyword","frequency"]).sort_values(by="frequency",ascending=False)

    keywords_df.to_csv("Milestone3_Keyword_Insights.csv",index=False)
    print("Milestone 3 completed Successfully")

    print(keywords_df.head(10))