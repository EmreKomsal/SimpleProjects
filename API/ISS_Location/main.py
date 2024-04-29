import requests
import tkinter as tk
import tkinterweb as tkweb
import folium as fm

url = "http://api.open-notify.org/iss-now.json"

try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.status_code)
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
    
data = response.json()["iss_position"]
print(data)

screen = tk.Tk()
screen.title("ISS Location")
screen.minsize(width=300, height=100)
screen.config(padx=20, pady=20)

def refresh():
    response = requests.get(url)
    data = response.json()["iss_position"]
    latitude.config(text=data["latitude"])
    longitude.config(text=data["longitude"])
    screen.after(5000, refresh)
    
def create_map():
    print("Creating map...")
    map_object = fm.Map(location=[float(data["latitude"]), float(data["longitude"])], zoom_start=5)
    fm.Marker(location=[float(data["latitude"]), float(data["longitude"])], popup="ISS Location", icon=fm.Icon(color="red")).add_to(map_object)
    print("Map created.")
    print("Saving map...")
    map_object.save("/Users/ekomsal/Projects/PythonProjects/SimpleProjects/API/ISS_Location/iss_location.html")
    print("Map saved.")
    return "/Users/ekomsal/Projects/PythonProjects/SimpleProjects/API/ISS_Location/iss_location.html"
    
def show_map():
    try:
        map_file = create_map()
        html_frame.load_file(map_file)
        print("Map loaded.")
    except Exception as e:
        print(f"Error occurred: {e}")

latitude_label = tk.Label(text="Latitude:", font=("Arial", 12, "bold", "underline"))
latitude_label.grid(row=0, column=0)

latitude = tk.Label(text=data["latitude"])
latitude.grid(row=0, column=1)

longitude_label = tk.Label(text="Longitude:", font=("Arial", 12, "bold", "underline"))
longitude_label.grid(row=1, column=0)

longitude = tk.Label(text=data["longitude"])
longitude.grid(row=1, column=1)

html_frame = tkweb.HtmlFrame(screen)
html_frame.grid(row=2, column=1, columnspan=2)
show_map()
    
screen.after(5000, refresh)
screen.after(5000, show_map)

screen.mainloop()


