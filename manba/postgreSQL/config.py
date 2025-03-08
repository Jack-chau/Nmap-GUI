from configparser import ConfigParser

def Connect2DB( 
        file_name='database.ini',
        section = 'postgresql'
    ):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read( file_name )
    db = dict()

    if parser.has_section( section ) :
        params = parser.items( section )
        for param in params:
            db[param[0]] = param[1]
        return db
    else :
        raise Exception( 'Section{0} is not found in the {1} file.'.format( section, file_name ) )