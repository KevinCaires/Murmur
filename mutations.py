from gql import gql


def set_player(nick):
    mutation ='''
        mutation{
            profileRegister(input:{
                discordId: "%s"
            }){
                profile{
                  id
                  discordId
                  expEarned
              }  
            }
        }
    ''' % nick
    print(mutation)
    return gql(mutation)
