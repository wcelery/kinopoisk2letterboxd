import pandas as pd
import html

k_import_filename = ""
k_import = open(k_import_filename, "r", encoding='utf-8')


'''
0 - Title
1 - Year
2 - WatchedDate
3 - Rating10
'''

movie_list = []
movie_list.append(['Title', 'Year', 'WatchedDate', 'Rating10'])
line_number = 0
Title_flag = 0
Year_flag = 0
WatchedDate_flag = 0

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

for line in k_import:
    line_number += 1
    movie_number = line_number//24 + 1

    # movie title starts after 5th comma, + 1 to exclude comma from the title
    movie_rating_index_start = find_nth(line, ',', 4) + 1
    movie_title_index_start = find_nth(line, ',', 5) + 1

    # movie title ends after 2th comma from the end
    movie_title_index_end = find_nth(line, ',', 6)

    movie_title = line[movie_title_index_start:movie_title_index_end]

    # append title
    movie_list.append([html.unescape(movie_title),'','', ''])

    # append watched date
    movie_list[line_number][2] = line[7:11]+'-'+line[4:6]+'-'+line[1:3]

    # append rating

    movie_list[line_number][3] = line[movie_rating_index_start:movie_title_index_start-1] 
    print(movie_list[line_number])
    # todo organize the code
    #Title
    '''if (line_number%24)%4 == 0 and (line_number%24 != 0) and Title_flag < movie_number:
        Title_flag += 1
        
        #Is title in english or in russian?
        if line[32:-6]:
            movie_list.append([html.unescape(line[32:-6]),'','', ''])
        else:
            movie_list.append([html.unescape(previous_line[35:-10]),'','', ''])
    #Year
    elif (line_number%24)%5 == 0 and (line_number%24 != 0) and Year_flag < movie_number:
        Year_flag += 1
        movie_list[movie_number][1] = line[25:-6]
    #WatchedDate
    elif (line_number%24)%23 == 0 and (line_number%24 != 0) and WatchedDate_flag < movie_number:
        WatchedDate_flag += 1
        movie_list[movie_number][2] = line[47:51]+'-'+line[44:46]+'-'+line[41:43]
    #Rating10
    elif (line_number%24)%11 == 0 and (line_number%24 != 0) and Rating10_flag < movie_number:
        Rating10_flag += 1
        movie_list[movie_number][3] = line[32:-6]

    #If there's only russian title
    previous_line = line'''

del movie_list[-1]
movie_df = pd.DataFrame(movie_list)

movie_df.to_csv('k_export.csv', index=False, header=False)

k_import.close()
