from models.entities.User import User

class ModelUser():

    @classmethod
    def LoggedUser(self,db,user):
        try:
            cursor=db.connect.cursor()
            QUERY_USER=""" SELECT IDADMIN,USERNAME,PASSWORD
                        FROM administrator 
                        WHERE USERNAME='{}'""".format(user.username)
            cursor.execute(QUERY_USER)
            answer=cursor.fetchone()
            if answer !=None:
                user=User(answer[0],answer[1],User.CheckPassword(answer[2],user.password))
                return user
            
            else:
                return None
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod    
    def GetById(self,db,id):
        try:
            cursor=db.connect.cursor()
            QUERY_ID=""" SELECT IDADMIN,USERNAME
                    FROM administrator
                    WHERE IDADMIN={}""".format(id)
            cursor.execute(QUERY_ID)
            answer=cursor.fetchone()
            if answer != None:
                user=User(answer[0],answer[1],None)
                return user

            else:
                return None
        except Exception as ex:
            return Exception(ex)
    

        