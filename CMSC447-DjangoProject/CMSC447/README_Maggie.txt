
In order to run this software:
1. Follow this tutorial to install django and python, as well as set up the necessary server: https://www.youtube.com/watch?v=VuETrwKYLTM
2. type 'workon (whatever you named your server in the previous step)' into an ide terminal compatible with python
3. type 'python manage.py (whatever you named your server in the previous step)' into the same terminal to start up the project server
4. available pages to view:
    (ip address)
        This page displays a list of strings. The plan is for the list to pull document titles 
        from the database and each title links to a page that displays that document open. 
    (ip address) + "/upload"
        This page allows the user to upload a file. The file is saved to the project's 'media' folder

Partial functionality: when uploading a file, an error is thrown: "no such table: documents_document". The upload still works, but there is an error.