import shutil

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.png*"),
                                                     ("all files",
                                                      "*.*")))

    shutil.copy(filename, f"C://Users//camer//OneDrive - Exeter College//python//github//pokemonDashboard//main//Pokemon Pictures//{name}")

button_explore = Button(root,
                        text="Browse Files",
                        command=browseFiles)

button_explore.place(relx=0.25, rely=0.5)
