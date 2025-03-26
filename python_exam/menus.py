import json
def show_main_menu(): 
    main_menu= """********Welcome*********
    1.show artist data
    2.quit
    """
    print(main_menu)
def ask_option():
    return input("type the desired option")
def show_artist_data():
    return show_artist_data    
    
while True:
 show_main_menu()
 opc=ask_option
 if opc == "1":
     show_artist_data()
 elif opc == "2":
     print("goodbye...")
     break
 else:print("wrong output")
     
def show_artist_data(): 
    artist_data="""*********Artist Data***********
    1.show all artist
    2.search artist data by
    3.add artist data
    4.add music genre
    5.quit
    """
    print(artist_data)
def ask_option():
    return input("type the desired option")
def show_artist_data_by():
   return show_artist_data_by
while True:
    show_artist_data()
    opc=ask_option()
    if opc == "1":
        print(json)
    elif opc == "2":
      show_artist_data_by
    elif opc == "3":
        def add_artist():
            new_art_data=input("enter the new artist data")
            for i in json:
                if i["artist"] == new_art_data:
                    print(json[i])
    elif opc == "4":
        def add_music_genre():
            new_music_genre=input("enter the new music genre")
            for i in json:
                if i["music_genre"] == new_music_genre:
                    print(json[i])
                elif opc == "5":
                    print("goodbye...")
                    break
                else:
                    print("wrong output")  
def show_artist_data_by():
    artist_data_by="""**********Search by***********
    1.search by name of the artist
    2.search by country of origin
    3.search by years of activity
    4.search by year of the first disk that reached lists
    5.search by music genre
    6.search by amount of certified units
    7.search by reclaimed units
    8.search by state of the artist
    9.search by date
    10.quit
    """
    print(artist_data_by)
def ask_option():
    return input("type the desired option")
artist_country="""*********Artist country*********
1.country name
2.country name and date
3.ISO code
4.quit"""
print(artist_country)
def ask_option():
    return input("type the desired option")