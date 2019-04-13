# coreyms_scrapper
Using BeautifulSoup and requests libraries to scrap a website.  

The main idea of this code is to grab information from  https://coreyms.com/ and pars it using lxml 

- The information are article posts which contain a headline summary and a video from youtube 

first we find all divs that contain the the class "article"

then the headline is taken from the h2 tage and <a> tage text

then the summary is taken from the div with the "entry-content" class and grabbing it's text.

lastly to get the link of the youtube video we have to parse the embeded youtube link.

by first taking the iframe with the class "youtube-player" and accessing the source attribute like a dictionary 

vid_src = article.find('iframe', class_='youtube-player')['src']

vid_id = vid_src.split('/')[4]

after splitting the content of the source at the "/" the video id is at the 4th index of the list 

tb8gHvYlCFs?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent

the video id is before the ? 

the real link for the video is at:
youtube_link = f"https://youtube.com/watch?v=tb8gHvYlCFs"

All of these information are loaded in a csv file.



