
In order to run this software:
1. Follow this tutorial to install django and python, as well as set up the necessary server: https://www.youtube.com/watch?v=VuETrwKYLTM
2. type 'workon (whatever you named your server in the previous step)' into an ide terminal compatible with python
3. type 'python manage.py (whatever you named your server in the previous step)' into the same terminal to start up the project server
4. available page to view:
    (ip address)
        This page is where the user logs in. 
        If the username is 'admin' and the password is also 'admin'
            (ip address)/'admin'
                This page is the admin dashboard. Here, they can upload files.
        If the username is 'student' and the password is also 'student'
            (ip address)/'student'
                This page is the student dashboard. Here, the user can view available assignements 

Partial functionality: when uploading a file, an error is thrown: "no such table: documents_document". The upload still works, but there is an error.