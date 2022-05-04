import xmlrpc.client

HOST = 'localhost'
PORT = '8569'
DB = 'o15-learn'
USER = 'admin'
PASS = 'admin'

root = 'http://%s:%s/xmlrpc/2/' % (HOST, PORT)
uid = xmlrpc.client.ServerProxy(root + 'common').login(DB, USER, PASS)
print("Logged in as %s (uid: %d)" % (USER, uid))

sock = xmlrpc.client.ServerProxy(root + 'object')

if uid:
    sessions = sock.execute(DB, uid, PASS, 'openacademy.sessions', 'search_read', [], ['name', 'number_of_seats'])
    for session in sessions:
        print("Session: %s (%s seats)" % (session['name'], session['number_of_seats']))

    args_course = [('name', 'ilike', 'Python')]
    course_list = sock.execute_kw(DB, uid, PASS, 'openacademy.course', 'search', [args_course])
    if course_list:
        course = course_list[0]
        args_session = [{'name': 'Session xml_rpc.py', 'course': course, 'duration': 10}]
        session_new = sock.execute_kw(DB, uid, PASS, 'openacademy.sessions', 'create', args_session)
        print("Created new session")
else:
    print("Error authorization!")
