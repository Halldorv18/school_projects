#definition for music_func goes here
def music_func(music = "Classic Rock", group = "The Beatles", singer = "Freddie Mercury"):
    print("The best kind of {} is {}".format("music", music))
    print("The best {} is {}".format("music group", group))
    print("The best {} is {}".format("lead vocalist", singer))



def main():
    
        music, group, singer = input("Input music, group, singer: ").split(',')
        music_func(music, group, singer)
        music_func()

main()