"""This is a programme which arranges examin scores and 
find the maximum/minmum number of the scores
"""
def average_score(scores):
	return sum(scores)/len(scores)
def sort_by_score(students):
	scores=[(students[k],k) for k in students]
	sort_score=sorted(scores,reverse=True)
	return sort_score
def max_score(lst):
	for i in lst:
		if i[0]==lst[0][0]:
			print i[1],i[0]
def min_score(lst):
	for i in lst:
		if i[0]==lst[-1][0]:
			print i[1],i[0]
examin_scores= {"google":98, "facebook":99, "baidu":52, "alibaba":80, "yahoo":49, "IBM":70, "android":76, "apple":99, "amazon":99}
print "average:"
print average_score(examin_scores.values())
print sort_by_score(examin_scores)
max_score(sort_by_score(examin_scores))
min_score(sort_by_score(examin_scores))
