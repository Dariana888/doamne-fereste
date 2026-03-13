import os

folder = input("Introdu calea către folder: ")
prefix = input("Introdu prefixul dorit pentru fișiere: ")
extension = input("Introdu extensia fișierelor (ex: .jpg, .png, .txt): ")

counter = 1

for file in os.listdir(folder):
    if file.endswith(extension):
        old_path = os.path.join(folder, file)
        new_name = f"{prefix}_{counter}{extension}"
        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)
        counter += 1

print("Redenumirea fișierelor s-a finalizat!")
