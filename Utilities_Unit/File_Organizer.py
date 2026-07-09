import os
import shutil

def main():
    while True:
        directory = input("Enter Folder Path:\n")

        check_flag = os.path.exists(directory)


        if check_flag :
            print(f"directory '{directory}' is True")
            check_directory = os.path.isdir(directory)

            if check_directory:
                print(f"directory '{directory}' is Folder")
            
                files = os.listdir(directory)

                for item in files:
                    result = os.path.join(directory , item) 

                    if os.path.isdir(result):
                        continue
                    else:
                        print(item)
                        file_name, file_format = os.path.splitext(item)
                        print(file_format)

                        if file_format.lower() in ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'):
                            directory_for_images = os.path.join(directory, "images")
                     
                            if os.path.exists(directory_for_images):
                                pass
                            else:
                                os.makedirs(directory_for_images)
                        
                            source_images = result
                            move_to = directory_for_images
                            images_folder = shutil.move(source_images, move_to)
                            print(f"all imagers move to '{directory_for_images}' directoty")
                    
                        elif file_format.lower() in ('.mp4', '.mkv', '.avi', '.mov', '.webm'):
                            directory_for_videos = os.path.join(directory, "videos")
                     
                            if os.path.exists(directory_for_videos):
                                pass
                            else:
                                os.makedirs(directory_for_videos)
                        
                            source_videos = result
                            move_to = directory_for_videos
                            image_folder = shutil.move(source_videos, move_to)
                            print(f"all imagers move to '{directory_for_videos}' directoty")

                        elif file_format.lower() in ('.mp3', '.wav', '.flac', '.aac', '.ogg'):
                            directory_for_music = os.path.join(directory, "music")

                            if os.path.exists(directory_for_music):
                                pass
                            else:
                                os.makedirs(directory_for_music)
                        
                            source_music = result
                            move_to = directory_for_music
                            image_folder = shutil.move(source_music, move_to)
                            print(f"all imagers move to '{directory_for_music}' directoty")

                        elif file_format.lower() in ('.pdf', '.doc', '.docx', '.txt', '.rtf'):
                            directory_for_Documents = os.path.join(directory, "Documents")
                     
                            if os.path.exists(directory_for_Documents):
                                pass
                            else:
                                os.makedirs(directory_for_Documents)

                            source_Documents = result
                            move_to = directory_for_Documents
                            image_folder = shutil.move(source_Documents, move_to)
                            print(f"all imagers move to '{directory_for_Documents}' directoty")

                        elif file_format.lower() in ('.zip', '.rar', '.7z', '.tar', '.gz'):
                            directory_for_Archives = os.path.join(directory, "Archives")
                     
                            if os.path.exists(directory_for_Archives):
                                pass
                            else:
                                os.makedirs(directory_for_Archives)
                        
                            source_Archives = result
                            move_to = directory_for_Archives
                            image_folder = shutil.move(source_Archives, move_to)
                            print(f"all imagers move to '{directory_for_Archives}' directoty")

                        elif file_format.lower() in ('.py', '.exe', '.msi', '.html'):
                            directory_for_Programs = os.path.join(directory, "Programs")
                     
                            if os.path.exists(directory_for_Programs):
                                pass
                            else:
                                os.makedirs(directory_for_Programs)
                        
                            source_Programs = result
                            move_to = directory_for_Programs
                            image_folder = shutil.move(source_Programs, move_to)
                            print(f"all imagers move to '{directory_for_Programs}' directoty")

                        else:
                            directory_for_others = os.path.join(directory, "others")

                            if os.path.exists(directory_for_others):
                                pass
                            else:
                                os.makedirs(directory_for_others)
                        
                            source_others = result
                            move_to = directory_for_others
                            image_folder = shutil.move(source_others, move_to)
            
                break_flag = input("do you want to continue? y/n\n")
            
                if break_flag.lower() == "n":
                    break          



            else:
                print(f"directory '{directory}' is not Folder")

                break_flag = input("do you want to continue? y/n\n")
            
                if break_flag.lower() == "n":
                    break
        else:
            print(f"directory '{directory}' is False")
            break_flag = input("do you want to continue? y/n\n")
            
            if break_flag.lower() == "n":
                break