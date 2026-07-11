import os 

def main():
    def checker(item_directory):
        files_list = []
        for item in os.listdir(item_directory):
            item_source_2 = os.path.join(item_directory, item)

            if not os.path.isdir(item_source_2):
                files_list.append(item_source_2)
            else:
                files_list.extend(checker(item_source_2))        

        return files_list


    while True:

        user_directory = input("enter directory for check:\n")

        if os.path.exists(user_directory):
            print(f"Directory {user_directory} is true")
        
            if os.path.isdir(user_directory):
            
                print(f"directory {user_directory} is folder addres")
                tag_list = []
                check = []
                for item in os.listdir(user_directory):
                    item_source = os.path.join(user_directory, item)
                    
                    if not os.path.isdir(item_source):
                        tag_list.append(os.path.join(user_directory, item))

                    else:                    
                        check.extend(checker(item_source))
                        
                final_list = (tag_list + check)        

                files_dict ={}

                for item in final_list:
                    key = os.path.basename(item)
                    Value = os.path.dirname(item)

                    if key in files_dict:
                        files_dict[key].append(Value)
                    else:
                        files_dict[key] = [Value] 

                
                for key in files_dict:
                    count = len(files_dict[key])
                    if count > 1:
                        print(f"'{key}' repeat '{count}' times on {files_dict[key]} directory")
                    else:
                        print(f"no duplicate file in {user_directory}")
            
            else:
                print(f"directory {user_directory} is file addres")

                continue_question = input("try again?y/n\n")

                if continue_question.lower() == "n":
                    break
                
        else:
            print(f"Directory {user_directory} is false")
            continue_question = input("try again?y/n\n")

            if continue_question.lower() == "n":
                break

if __name__ == "__main__":
    main()