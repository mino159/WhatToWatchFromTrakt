import requests
from random import choice

username="mino159"		#your nick on trakt.tv

def main():
	all_titles=giveList()
	print(choice(all_titles)) #choose one item from whole list

def giveList():
	"""Go on website and return all titles from watchlist"""
	url=f"https://trakt.tv/users/{username}/watchlist"
	response = requests.get(url)
	all_titles=find_all(response.text,"<div class=\"titles\"><h3>","<")
	return all_titles


def find_all(a_str : str, sub_start : str, sub_end : str):
	"""Return strings between sub_start and sub_end in a_str"""
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
