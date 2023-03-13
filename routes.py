from resources import  showStudentsApi,booksApi,updateBook

def initialize_routes(api):
    api.add_resource(showStudentsApi, '/api/showStudents')
    api.add_resource(booksApi,'/api/showAllBooks')
    api.add_resource(updateBook,'/api/updateBook/<id>')
