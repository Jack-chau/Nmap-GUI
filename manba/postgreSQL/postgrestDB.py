import psycopg2
from configparser import ConfigParser

class ConfigDB(  ) :

    def Connect2DB( 
            self, 
            file_name = 'database.ini', 
            section = 'postgresql' 
    ) :
        self.parser = ConfigParser( )
        self.parser.read( file_name )
        db = dict( )

        if self.parser.has_section( section ) :
            self.params = 



    def DBVersion( self ) :
        connection = None
        try :
            params = config_DB()
            print( 'Connecting to the postgreSQL database.....')
            connection = psycopg2.connect(**params)

            # creata a cursor
            cursor = connection.cursor( )
            print( 'postgreSQL database version: ')
            cursor.execute( "SELECT version()" )
            db_version = cursor.fetchall( )
            print( db_version )
            cursor.close()
        except( Exception, psycopg2.DatabaseError ) as error :
            print( error )
        finally :
            if connection is not None :
                connection.close()
                print( 'Database connection terminated' )
if __name__ == "__main__" :
    a = connect()
    a.connect_db()


    