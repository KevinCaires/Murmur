from gql import gql


def catch_item(item):
    mutation ='''
    mutation{
    addItemToBag(
      input:{
        discordId: "baz"
        itemName: "Silvertape"
        qt: 3
  }){
    profile{
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
    '''
    return gql(mutation)


def drop_item():
    mutation = '''
    mutation{
  removeItemFromBag(input: {
    discordId: "baz"
    itemName: "Silvertape"
    qt: 4
  }){
    profile{
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
    '''
    return gql(mutation)
