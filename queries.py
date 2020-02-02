from gql import gql


def get_location(player):
    query = '''
query{
  profiles(discordId: "%s"){
    edges{
      node{
        id
        discordId
        expEarned
        isDead
        life
        actualPosition
        actualZone{
          zoneReference
        }
        actualArea{
          areaReference
          areaRowMaxSize
          areaColumnMaxSize
        }
        bag{
          edges{
            node{
              id
              name
              description
            }
          }
        }
      }
    }
  }
}''' % player
    return gql(query)


def is_dead():
    query = '''
    query{
      profiles(isDead: true){
        edges{
          node{
            id
            discordId
            expEarned
            isDead
            life
            actualPosition
            actualZone{
              zoneReference
            }
            actualArea{
              areaReference
              areaRowMaxSize
              areaColumnMaxSize
            }
            bag{
              edges{
                node{
                  id
                  name
                  description
                }
              }
            }
          }
        }
      }
    }'''
    return gql(query)

def bag_itens(player):
    query = '''
    query{
      profiles(discordId: "%s"){
        edges{
          node{
            bag{
              edges{
                node{
                  id
                  name
                  description
                }
              }
            }
          }
        }
      }
    }''' % player
    return gql(query)
