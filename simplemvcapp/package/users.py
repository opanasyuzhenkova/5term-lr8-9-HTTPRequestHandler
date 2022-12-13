from simplemvcapp.models import *


def get_users_lst():
    user1 = zhukov.Zhukov()
    userDenis = ignatev.Ignatev()
    userIvan = ivan.Ivan()
    userIvanova = ivanova.Ivanova()
    userSergeeva = sergeeva.Sergeeva()
    userShchegolskiy = shchegolskiy.Shchegolskiy()
    userEgor = sobinin.Sobinin()
    userAndrew = logwinow.Logwinow()
    userMatvey = zhuravskiy.Zhuravskiy()
    userSmirnov = smirnov.Smirnov()
    userPanasyuzhenkova = panasyuzhenkova.Panasyuzhenkova()

    user_lst = [user1, userDenis, userEgor, userSmirnov, userPanasyuzhenkova, userIvan, userAndrew, userMatvey,
                userSergeeva, userIvanova, userShchegolskiy]

    user_dict = {}

    for idx, item in enumerate(user_lst):
        user_dict[idx+1] = list(item.full_name.strip().split(' '))

    return user_dict