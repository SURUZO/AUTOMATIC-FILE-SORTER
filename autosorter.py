import os
import shutil
import sys

def organize_files():
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
        'Documents': ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Executables': ['.exe', '.msi', '.bat', '.sh'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Code': ['.py', '.java', '.cpp', '.html', '.css', '.js'],
        'Spreadsheets': ['.csv', '.xls', '.xlsx'],
        'Presentations': ['.ppt', '.pptx'],
        'Scripts': ['.sh', '.bash', '.ps1'],
        'Text': ['.txt', '.md', '.markdown'],
        'Web': ['.html', '.css', '.js', '.php'],
        'Fonts': ['.ttf', '.otf'],
        'CAD': ['.dwg', '.dxf'],
        'Database': ['.sql'],
        'Ebooks': ['.epub', '.mobi'],
        'Virtual Machines': ['.ova', '.vmdk', '.vmx'],
        'GIS': ['.shp', '.kml', '.kmz'],
        'Game Files': ['.unity', '.gmx', '.apk'],
        'Miscellaneous': ['.dat', '.ini', '.cfg', '.log', '.bak'],
        'Images Raw': ['.raw', '.nef', '.cr2'],
        'Vector Graphics': ['.svg', '.ai', '.eps'],
        '3D Models': ['.obj', '.fbx', '.stl'],
        'Medical Images': ['.dicom'],
        'Backup Files': ['.bak', '.backup'],
        'Logs': ['.log'],
        'Torrents': ['.torrent'],
        'Emails': ['.eml', '.msg'],
        'Certificates': ['.crt', '.pem'],
        'Virtual Reality': ['.vr'],
        'Calendars': ['.ics'],
        'Mind Maps': ['.mm', '.mindmap'],
        'Databases': ['.db', '.sqlite', '.dbf'],
        'Project Files': ['.project', '.sln', '.xcodeproj'],
        'Other': [],  # Generic category for unknown or miscellaneous files
    }

    script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
    exe_name = 'AutoSorter.exe' if getattr(sys, 'frozen', False) else 'AutoSorter.py'

    for file in os.listdir(script_directory):
        if file == exe_name:
            continue

        file_path = os.path.join(script_directory, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()

            category = 'Other'
            for key, extensions in file_types.items():
                if file_extension in extensions:
                    category = key
                    break

            folder_path = os.path.join(script_directory, category)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            try:
                destination_path = os.path.join(folder_path, file)
                counter = 1
                while os.path.exists(destination_path):
                    base_name, extension = os.path.splitext(file)
                    new_file_name = f"{base_name}_{counter}{extension}"
                    destination_path = os.path.join(folder_path, new_file_name)
                    counter += 1

                shutil.move(file_path, destination_path)
                print(f"Moved {file} to {category} folder as {os.path.basename(destination_path)}.")

            except (PermissionError, FileNotFoundError) as e:
                print(f"Error moving {file}: {e}")

if __name__ == "__main__":
    organize_files()
