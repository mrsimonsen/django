# django
for learning django
Now for making a blog site

[Django Web Framework Class from moz://a](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

[\*Current Section\*](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#How_to_run_the_tests)

## upgrade Notes:
* I liked the idea of writing blog posts in markdown then having them converted to html [this may work](https://www.imzjy.com/blog/2018-05-20-render-the-markdown-in-django)

### Additional Resources
[for live preview of markdown](https://markdownlivepreview.com/)
[auto deploy to server](https://dev.to/p0oker/automatic-deployment-from-github-to-your-server-with-no-third-party-app-3f5j)


### setup notes:
* not using a virtual environment since it will be deployed on a self contained codeanywhere virtual machine/raspberry pi server
* special set up to work in codeanywhere:
  * Right-click on container > config. Add "python path_to/manage.py runserver 0.0.0.0:8000" to the command list"
  * Edit settings.py and add your codeanywhere app url to the ALLOWED_HOSTS list.
    * format: **container**-**username**.codeanyapp.com
* don't forget to set TIME_ZONE = 'America/Denver' in settings.py
