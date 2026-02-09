from User import User
from datetime import date

def is_legal_age_decorator(func):
    def wrapper(user: User, *args, **kwargs):
            
        if not isinstance(user, User):
            raise TypeError("El parametro debe ser de tipo User")
        
        if user.age < 18:
            raise PermissionError(
                f"El usuario tiene edad de {user.age} años, no es mayor de edad"
            )
            
        return func(user,*args, **kwargs)
            
    return wrapper

@is_legal_age_decorator
def vote_for_president(user: User, vote):
    print(f"El usuario de edad {user.age} puede votar y lo hace por {vote}")


def main():
    user_1 = User(date(2005, 10, 31))
    user_2 = User(date(2008, 2, 9))
    user_3 = User(date(2008, 2, 10))
    user_4 = User(date(1999, 10, 31))
    
    
    vote_for_president(user_1, 'PPSO')
    vote_for_president(user_2, 'PLN')
    vote_for_president(user_3, 'PAC')
    vote_for_president(user_4, 'FA')


main()