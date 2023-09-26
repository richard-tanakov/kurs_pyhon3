match vacancies := str(input()):
    case 'Flask' |'Django' |'Fast-API': #Python
        print('Python','(',vacancies,')',',Backend-dev', sep='')
    case 'Angular'|'React'|'Vue':
        print('JavaScript/TypeScript','(', vacancies,')',',Frontend-dev', sep='')
    case 'Flutter' |'React Native':
        print( 'JavaScript','(',vacancies,')',',Cross-Mobile-dev', sep='')
    case 'Pandas' |'skit-learn'|'keras':
        print('Python','(',vacancies,')',',Data-Scientist', sep='')
    case _:
        print("модель еще не обучена")