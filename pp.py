import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


print('Enter some skills you are not familiar with')
inputs =[]
while True:
    unfamiliar_skills = input('>')
    unfamiliar_skill= unfamiliar_skills.upper()
    if not unfamiliar_skill:
         break
    inputs.append(unfamiliar_skill)
set_inputs = set(inputs)


print(f'Fileterin out : {unfamiliar_skill}')
company_name = []
skills_required = []
more_links =[]

def find_jobs():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation="
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published = job.find('span',class_='sim-posted').span.text
        if 'few' in published:

            company= job.find('h3',class_='joblist-comp-name').text.replace('  ','')
            skills = job.find('span',class_='srp-skills').text.replace('  ','')
    
            skills_unfamiliar = [i.strip() for i in skills.split(',')]
            # print(skills_unfamiliar)
            converting_to_upper_skills = [i.upper() for i in skills_unfamiliar]
            set_skills = set(converting_to_upper_skills)
            # print(set_skills )

            if not set_inputs.intersection(set_skills):
                    
                    more_info = job.header.h2.a['href']
                    company_name.append({company.strip()})
                    skills_required.append({skills.strip()})
                    more_links.append({more_info})                    
                

if  __name__ == '__main__':
   
          find_jobs()
          data = {'Company name':company_name, 'Skills required':skills_required,'More Info':more_links}
          df = pd.DataFrame(data)

          df.to_excel('job_listing.xlsx',index=False)
          print('Data has been saved ')
        #   time_wait = 10
        #   print(f"waiting {time_wait} seconds")
        #   time.sleep(time_wait*60)
        