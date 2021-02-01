admin="User"
pas=123
import os
while(True):
    print("--------WELCOME TO THE BLOG PAGE---------")
    print("HAPPY TO SEE YOU HERE  :)")
    print("Press 1.--> to login")
    print("Press 2.--> to quit")
    main_choice=int(input("Enter your choice:"))

    while (True):
        if(main_choice==1):
            print("<--------------WELCOME TO THE LOGIN PAGE---------------->")
            print("If you want to go to back menu press 2")
            user_id=input("please enter your User ID:").capitalize()
            if user_id==admin:
                print("User ID is matched")
                user_pass=int(input("please enter your password to proceed login"))
                if user_pass==pas:
                    print("logged in successfully")
                    while(True):
                        print("press 1. --> for create section")
                        print("press 2. --> for read section")
                        print("press 3. --> for delete section")
                        print("press 4. --> for logout and quit")
                        user_choice = int(input("enter your choice"))
                        while(True):
                            if user_choice == 1:
                                print("press 1. --> for new blog")
                                print("press 2. --> for editing blog")
                                print("press 3. --> for going back")
                                choice3 = int(input("enter your choice"))
                                if (choice3==1):
                                    new_blog_name=input("enter the name of the new blog").capitalize()
                                    name1=open(new_blog_name,'x')
                                    new_blog_content=input("enter the content of new blog:")
                                    name1.write(new_blog_content)
                                    name1.close()
                                    print("Blog created successfully")
                                    break
                                elif (choice3==2):
                                    edit=input("enter the name of blog which you want to edit:").capitalize()
                                    if os.path.exists(edit):
                                        print("match found")
                                        print("what you want to do??")
                                        print("press 1. --> for overwrite")
                                        print("press 2. --> for adding")
                                        editchoice=int(input("enter your choice:"))
                                        if editchoice==1:
                                            edit_blog_name=input("enter the name again").capitalize()
                                            name2=open(edit_blog_name,'w')
                                            edit_content = input("enter the content that is to be overwritten:")
                                            name2.write(edit_content)
                                            name2.close()
                                            print("blog overwitten")

                                        elif editchoice==2:
                                            edit_blog_name2=input("enter the name again").capitalize()
                                            name3=open(edit_blog_name2,'a')
                                            edit_content2=input("enter the content that is to be appended")
                                            name3.write(edit_content2)
                                            name3.close()
                                            print("blog appended")


                                    else:
                                        print("doesn't match")
                                        break
                                elif choice3==3:
                                    break
                            elif user_choice == 2:
                                print("WELCOME TO READ SECTION")
                                read_choice = input("Please enter the file name").capitalize()
                                if os.path.exists(read_choice):
                                    fun = open(read_choice, 'r')
                                    print(fun.read())
                                    break
                                else:
                                    print("File does not exists")
                                    break

                            elif(user_choice==3):
                                print("Enter the name of the blog ")
                                delete_name = input().capitalize()
                                if os.path.exists(delete_name):
                                    os.remove(delete_name)
                                    print("The file has been deleted")
                                    break
                                else:
                                    print("file not found")
                                    break
                            else:
                                print("thank you")
                                exit()



                    else:
                        print("oops! wrong password")
                        break


            elif user_id=='2':
                break


            else:
                print("oops! User ID did'nt matched")
                print("please enter correct ID")
                break

        elif(main_choice==2):
            print("THANK YOU FOR USING OUR BLOG SERVICE")
            print("SEE YOU SOON   :)")
            exit()
        else:
            print("oops!! Please enter the correct choice")
            break
