# hellodjango-cc
Crash Course (Wedge) of Django book project.

## Django Project vs Apps
- A Django project is a folder containing all the code
(Python, templates, etc.) needed to run a website.
- A Django app is a folder within a Django project.
- Django apps are isolated components that do one
specific thing in a Django project.
- Combining Django apps is one of the primary
things we do when we build a Django project

## Understanding Views & TemplateView Class:
- Views are how a Django project communicates with
the user. They send out web pages, JSON, spreadsheets, PDFs, and so much more.
- Templates are often used by views to render HTML
for web pages.
- A TemplateView renders a Django template and sends
it to a browser.

### Useful commands
`pip install -r requirements.txt`
`pip freeze > requirements.txt`