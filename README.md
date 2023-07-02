#FSDI-Capstone Final Project

Old Dogs-New Tricks is a simple blog website for digitally challenged people who want to learn about
software development topics.
 

It has basic navbar functions i.e., Home, About, Contact, Log In, Sign Up links for visitors. If logged in as a user the link functions of View All Post, Add A Post, and Log Out then become available.

It relies on Django based authentication and authorization functions for signing up / logging in, as well as “Forgot Your Password” and “Reset Your Password” functions (the message gets sent to the console). 

The blog post functions for authorized users are fully CRUD compliant and include; Add A Post, Edit Post, Delete Post, Comment on a Post, and Like or Dislike functions for each post with a Current Count display. The posts are viewable as a truncated list or in detail view which includes the author and date of creation.

This website was developed using Django – Python, and CSS, HTML.

I used Windows PowerShell for the command line, and the program runs in a virtual environment using .venv\Scripts\activate. From there the program runs on the development server at http://127.0.0.1:8000/ with the standard starting command of: py  manage.py  runserver
