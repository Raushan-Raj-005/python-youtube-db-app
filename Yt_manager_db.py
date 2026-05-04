import sqlite3

conn = sqlite3.connect('Yt_videos.db')

cursor = conn.cursor()

cursor.execute('''
     CREATE TABLE IF NOT EXISTS VIDEOS(
         id INTEGER PRIMARY KEY,
         name TEXT NOT NULL,
         time TEXT NOT NULL
     )         
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("Empty Database")
    else:   
        for row in rows:
            print(row)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)",(name, time))
    conn.commit()
    
def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id =?", (new_name, new_time, video_id))
    conn.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()



def main():
    while True:
        print("\n Youtube manager app with db")
        print("1. list all videos")
        print("2. Add a  videos")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5.  Exit app")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\n", "`" * 50)
            list_videos()
            print("\n", "`" * 50)
            
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)    
        elif choice == '3':
            video_id = input("Enter video id to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_videos(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video id to delete: ")
            delete_videos(video_id)    
        elif choice == '5':
            break   
        else:
            print("Invalid Choice") 

    conn.close()            
                

if __name__ == "__main__":
    main()
    