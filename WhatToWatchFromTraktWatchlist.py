import requests
from random import choice

username="mino159"		#your nick on trakt.tv

def main():
	all_titles=giveList()
	print(choice(all_titles))

def giveList():
	url=f"https://trakt.tv/users/{username}/watchlist"
	response = requests.get(url)
	# print(response.text)
	all_titles=find_all(response.text,"<div class=\"titles\"><h3>","<")
	return all_titles


def find_all(a_str, sub_start,sub_end):
	"find all the titles of games"
	names=[]
	start = 0;
	while True:
		name_starts = a_str.find(sub_start, start)
		# print(finding)
		if name_starts == -1: 
			break
		start = name_starts + len(sub_start)
		name_ends= a_str.find(sub_end,start)
		name=a_str[start:name_ends]
		# print(name)

		names.append(name)
		
	return names

main()