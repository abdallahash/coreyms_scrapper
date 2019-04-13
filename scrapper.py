from bs4 import BeautifulSoup 
import lxml
import requests 
import csv 

source = requests.get("https://coreyms.com/").text 

soup = BeautifulSoup(source, "lxml")

csv_file = open('corey_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video link'])

for article in soup.find_all('article'):
    #loop throw all the article on the website.

    headline = article.h2.a.text 
    print(headline)

    summary = article.find('div', class_='entry-content').text
    print(summary)

    # To make sure that if a link is missing we don't get into crazy error.
    try:

        #The link to the video is in an iframe that have a class called 'youtube-player'
        vid_src = article.find('iframe', class_='youtube-player')['src']
        #To access the attributs of a tag we need to access it like a dictionary.

        vid_id = vid_src.split('/')[4]
        vid_real_id = vid_id.split('?')[0]

        youtube_link = f"https://youtube.com/watch?v={vid_real_id}"
        print(youtube_link)
    except Exception as e:
        youtube_link = None
        print(youtube_link)

    print('------------------------------------------------------------------------------------------------------\n')

    csv_writer.writerow([headline, summary, youtube_link])

csv_file.close()




