![](https://nickandnataliebautista.com/static/icons/floral.png)![](https://nickandnataliebautista.com/static/icons/bride-ring.png)![](https://nickandnataliebautista.com/static/icons/wedding-cake.png)
# BoatParty
a.k.a. our wedding website

Why is this called BoatParty? If you don’t know, I love to fish and I’ve always dreamed of owning a bass boat. I used to joke with Natty that I’d buy a bass boat before I bought her an engagement ring. But of course, I didn’t do that and now we like to joke that my bass boat is sitting on her hand. Also, adding the word “wedding” in front of anything immediately makes it 10 times more expensive so we decided to stop using the W word! Thus, we’re calling this the BoatParty website.

## Tech Stack
* Programming Language - Python
* Web Framework - Flask
* Web Server - Nginx
* Database - MySQL
* Front End - HTML, CSS, Bootstrap, Javascript
* Tests - Unittest

## Features
While this website isn’t particularly complex, there are a couple of cool features that were fun to build.  
`Guest Book Posts` - It’s fun to leave people messages with stories or memories from the past so I created a guestbook. I used [Flask-Pagedown](https://github.com/miguelgrinberg/Flask-PageDown) so that users can get a little fancier with their formatting and use Markdown, if they so choose. Since we have some jokester friends who may be tempted to leave inappropriate messages, I added email notifications for new posts to help moderate any questionably content.  
`FAQ Emails` - While we tried to think of all the questions people might ask us, inevitably, we missed something. Since I configured email notifications for the Guest Book, I added an email form to the FAQ page so that users can send us a quick question they may have before they forget.

Resources that helped me get this up and running!  
[Flask Web Development: Developing Web Applications with Python 2nd Edition](https://www.amazon.com/Flask-Web-Development-Developing-Applications/dp/1491991739/ref=dp_ob_title_bk)  
[Corey Schafer - Flask Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)  
[Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ/search?query=flask)  
[CodeTime - Getting Started with Bootstrap4](https://www.youtube.com/playlist?list=PLylMDDjFIp1A3sMkpWwbIsQ8l8bZcIBmC)  
[Epic Bootstrap - Lightbox Gallery](https://epicbootstrap.com/snippets/lightbox-gallery)