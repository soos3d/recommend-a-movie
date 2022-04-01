import requests
import json

# function to get movie recommendations from tastedive.com API
def get_movies(title):

    base_url = ('https://tastedive.com/api/similar') 
    query_param = {'q': title  , 'type' : 'movies'}                 # spefify parameters
                                         
    api_call = requests.get(base_url , params = query_param)        # connects and retives data from the URL
                                                                  
    content = api_call.json()                                       # turn JSON into a python object
    #print(json.dumps(content, indent=2))                           # print the JSON in a more clear way
    
    # create a list of titles
    result=[]
    for titles in content['Similar']['Results']:        
        result.append(titles['Name'])                               # adds the name of the movie to the list
    
    # check for titles in the list
    if len(result) == 0:
        print('We did not find any movie to recommend! Make sure it is spelled correctly, or try another one')
    else:

        # format the titles if any has been received 
        for title in result:
            print('You might like: ', title)

# what the user sees and intercacts with
print('Get movies recommendations based on a movie you like!')
print('--------------------------------------' + '\n')
user_input = input("Type a movie that you like: ")

# call the function
get_movies(user_input)
