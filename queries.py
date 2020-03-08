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
    query profiles{
  profiles{
    edges{
      node{
        id
        discordId:"%s"
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
              item{
                name
              }
              stock
            }
          }
        }
      }
    }
  }
}''' % player
    return gql(query)


def especific_item(item):
    query = '''
   query{
  items(name: "%s"){
    edges{
      node{
        name
        description
        weight
      }
    }
  }
}
    ''' % item
    return gql(query)


def bot_profile(name):
  query = '''
  query{
  botProfiles(botName:"%s"){
    edges{
      node{
        botName
      }
    }
  }
}
  ''' % name
  return gql(query)

def bot_history(name):
  query = '''query{
  botProfiles(botName:"%s"){
    edges{
      node{
        botHistory
      }
    }
  }
} ''' % name
  return gql(query)